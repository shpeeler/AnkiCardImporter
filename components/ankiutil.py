# -*- coding: utf-8 -*-

import json
import re
import arabic_reshaper
from bidi.algorithm import get_display

from .config.configmanager import ConfigManager
from .ankiconnector import AnkiConnector
from .audiogenerator import AudioGenerator
from .jsonbuilder import JsonBuilder
from .xmlparser import XMLParser
from random import shuffle

class AnkiUtil(object):
    
    configmanager = None

    def __init__(self, configmanager):

        self.configmanager = configmanager

        self.ankiconnector = AnkiConnector(self.configmanager.Address)
        self.audiogenerator = AudioGenerator(self.configmanager.LanguageCode, self.configmanager.FileDestination)
        self.builder = JsonBuilder()

        existing_cards = None
        if self.configmanager.CheckExisting == True:
            existing_cards = self._get_existing_card_names()

        self.xmlparser = XMLParser(self.audiogenerator, self.builder, existing_cards)
        
    def create_cards_from_file(self, phrase_mode):
        
        if phrase_mode:
            cardsToAdd = self.xmlparser.parse_sentence(self.configmanager.FileSource, self.configmanager.SheetName, self.configmanager.LanguageCode, self.configmanager.Deck)
        else:
            cardsToAdd = self.xmlparser.parse_word(self.configmanager.FileSource, self.configmanager.SheetName, self.configmanager.LanguageCode, self.configmanager.Deck)
            
        if not cardsToAdd:
            print("error while reading the file: {0} with the language {1}".format(self.configmanager.FileSource, self.configmanager.LanguageCode))
            return
            
        total = len(cardsToAdd)

        if self.configmanager.SkipStore:
            print("skipping insert of {0} cards".format(total))
            return
        
        if self.configmanager.RandomInsert:
            shuffle(cardsToAdd)

        counter = 1
        for card in cardsToAdd:
            response = self.ankiconnector.post(card)
            print("{0}/{1} finished - {2}".format(counter, total, response.content))
            counter = counter + 1

    def clean_card(self):
        query_note_ids = self.builder.find_note_ids(self.configmanager.QueryDeck)
        response_note_ids = self.ankiconnector.post(query_note_ids)
        note_ids = json.loads(response_note_ids.content)["result"]

        query_note_info = self.builder.get_note_info(note_ids)
        response_note_info = self.ankiconnector.post(query_note_info)
        note_info = json.loads(response_note_info.content)["result"]

        counter = 1
        for each_info in note_info:

            note_id = each_info["noteId"]
            word = each_info["fields"]["Word"]["value"]
            translation = each_info["fields"]["Translation"]["value"]

            if "<div>" in word:

                word_clean = word.replace("<div>", "").replace("</div>", "")

                print("{} - {} -> {}".format(counter, word, word_clean))

                update_json = self.builder.update_name(note_id, word_clean)

                if self.configmanager.SkipStore == True:
                    continue
                
                self.ankiconnector.post(update_json)
            
            counter = counter + 1

    def _load_cards_by_query(self, query):
        query_note_ids = self.builder.find_note_ids(query)
        response_note_ids = self.ankiconnector.post(query_note_ids)
        note_ids = json.loads(response_note_ids.content)["result"]

        query_note_info = self.builder.get_note_info(note_ids)
        response_note_info = self.ankiconnector.post(query_note_info)
        note_info = json.loads(response_note_info.content)["result"]

        return note_info

    def _get_existing_card_names(self):
        result = list()
        
        cards_repo = self._load_cards_by_query(self.configmanager.Query)
        cards_deck = self._load_cards_by_query(self.configmanager.QueryDeck)

        result = self._return_names_from_info_clean(cards_repo) + self._return_names_from_info_clean(cards_deck)

        return result

    def _return_names_from_info_clean(self, note_info):
        result = list()

        for each_info in note_info:
            word = self._get_word_base(each_info)

            if word == None:
                raise Exception("field value coult not be found for: {0}".format(each_info))

            word_clean = word.replace("<div>", "").replace("</div>", "")

            result.append(word_clean)

        return result

    def _get_word_base(self, note_info):
        try:
            return note_info["fields"]["Word"]["value"]
        except:
            return None

    def add_audio_to_card_in_deck(self, force = False, plural = False, reshape = False):
        note_info = self._load_cards_by_query(self.configmanager.Query)
        clean_re = re.compile('<.*?>')

        counter = 1
        for each_info in note_info:
            
            note_id = each_info["noteId"]
            word = each_info["fields"]["Word"]["value"]
            audio = each_info["fields"]["Audio"]["value"]
            
            print_word = word
            if reshape == True:
                reshaped_text = arabic_reshaper.reshape(word)
                print_word = get_display(reshaped_text)

            query_add_audio = None
            query_add_audio_plural = None
            
            if audio == "" or force == True:
                tagless_word = re.sub(clean_re, '', word)
                clean_word = tagless_word.replace("&nbsp;", " ")

                self.audiogenerator.speak(clean_word)
                query_add_audio = self.builder.add_audio_by_id(note_id, self.configmanager.LanguageCode, clean_word)
                print("{}/{} new audio - {}".format(counter, len(note_info), print_word))

            if plural == True:
                audio_plural = each_info["fields"]["Audio Plural"]["value"]
                word_plural = each_info["fields"]["Word Plural"]["value"]

                if word_plural != "" and (audio_plural == "" or force == True):
                    plural_tagless_word = re.sub(clean_re, '', word_plural)
                    plural_clean_word = plural_tagless_word.replace("&nbsp;", " ")

                    self.audiogenerator.speak(plural_clean_word)
                    query_add_audio_plural = self.builder.add_audio_by_id_plural(note_id, self.configmanager.LanguageCode, plural_clean_word)
                    print("{}/{} new plural-audio - {}".format(counter, len(note_info), print_word))
            
            if self.configmanager.SkipStore == False:
                    if query_add_audio != None:
                        response_add_audio = self.ankiconnector.post(query_add_audio)

                    if query_add_audio_plural != None:
                        response_add_audio = self.ankiconnector.post(query_add_audio_plural)

            print("{}/{} - {}".format(counter, len(note_info), print_word))
            counter = counter + 1