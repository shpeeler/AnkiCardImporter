# -*- coding: utf-8 -*-

import json
import re
import arabic_reshaper
from bidi.algorithm import get_display

from .config.configmanager import ConfigManager
from .ankiconnector import AnkiConnector
from .audiogenerator import AudioGenerator
from .jsonbuilder import JsonBuilder
from .csvparser import CSVParser
from random import shuffle

class AnkiUtil(object):
    
    configmanager = None

    def __init__(self, configmanager):

        self.configmanager = configmanager

        self.ankiconnector = AnkiConnector(self.configmanager.Address)
        self.audiogenerator = AudioGenerator(self.configmanager.LanguageCode, self.configmanager.FileDestination)
        self.builder = JsonBuilder()
        self.csvparser = CSVParser(self.audiogenerator, self.builder)
        
    def create_cards_from_file(self):
        
        cardsToAdd = self.csvparser.parse(self.configmanager.FileSource, self.configmanager.LanguageCode)
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

    def add_audio_to_card_in_deck(self, force = False, plural = False, reshape = False):

        query_note_ids = self.builder.find_note_ids(self.configmanager.Query)
        response_note_ids = self.ankiconnector.post(query_note_ids)
        note_ids = json.loads(response_note_ids.content)["result"]

        query_note_info = self.builder.get_note_info(note_ids)
        response_note_info = self.ankiconnector.post(query_note_info)
        note_info = json.loads(response_note_info.content)["result"]

        clean_re = re.compile('<.*?>')

        counter = 1
        for each_info in note_info:
            
            note_id = each_info["noteId"]
            word = each_info["fields"]["Word"]["value"]
            audio = each_info["fields"]["Audio"]["value"]
            translation = each_info["fields"]["Translation"]["value"]
            
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
                word_plural = each_info["fields"]["Plural"]["value"]

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