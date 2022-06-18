# -*- coding: utf-8 -*-

import json
import re
import arabic_reshaper
from bidi.algorithm import get_display

from .ankiconnector import AnkiConnector
from .audiogenerator import AudioGenerator
from .jsonbuilder import JsonBuilder
from .csvparser import CSVParser
from random import shuffle


class AnkiUtil(object):
    
    def __init__(self, language, filedest, address):
        self.ankiconnector = AnkiConnector(address)
        self.audiogenerator = AudioGenerator(language, filedest)
        self.builder = JsonBuilder()
        self.csvparser = CSVParser(self.audiogenerator, self.builder)
        self.language = language
        
    def create_cards_from_file(self, filesrc, skip_store, random):
        
        cardsToAdd = self._read_cards_from_file(filesrc)
        if not cardsToAdd:
            print("error while reading the file: {0} with the language {1}".format(filesrc, self.language))
            return
            
        total = len(cardsToAdd)

        if skip_store:
            print("skipping insert of {0} cards".format(total))
            return
        
        if random:
            shuffle(cardsToAdd)

        counter = 1
        for card in cardsToAdd:
            print("inserting cards {0}/{1}".format(counter, total))
            response = self.ankiconnector.post(card)
            print(response.content)
            counter = counter + 1

    def add_audio_to_card_in_deck(self, query, skip_store, force, plural, reshape):

        query_note_ids = self.builder.find_note_ids(query)
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
                query_add_audio = self.builder.add_audio_by_id(note_id, self.language, clean_word)

            if plural == True:
                audio_plural = each_info["fields"]["Audio Plural"]["value"]
                word_plural = each_info["fields"]["Plural"]["value"]

                if word_plural != "" and (audio_plural == "" or force == True):
                    plural_tagless_word = re.sub(clean_re, '', word_plural)
                    plural_clean_word = plural_tagless_word.replace("&nbsp;", " ")

                    self.audiogenerator.speak(plural_clean_word)
                    query_add_audio_plural = self.builder.add_audio_by_id_plural(note_id, self.language, plural_clean_word)
            
            if skip_store:
                    print("{}/{} skipped - {}".format(counter, len(note_info), print_word))
                    counter = counter + 1
                    continue
            
            if query_add_audio != None:
                print("{}/{} audio added - {}".format(counter, len(note_info), print_word))
                response_add_audio = self.ankiconnector.post(query_add_audio)

            if query_add_audio_plural != None:
                print("{}/{} plural added - {}".format(counter, len(note_info), print_word))

                response_add_audio = self.ankiconnector.post(query_add_audio_plural)

            print("{}/{} finished - {}".format(counter, len(note_info), print_word))
            counter = counter + 1

    def _read_cards_from_file(self, filesrc):
        
        cardsToAdd = None
        
        if(self.language == 'pl'):
            print("starting parser in polish mode")
            cardsToAdd = self.csvparser.parse_pl(filesrc)
            
        if(self.language == 'fr'):
            print("starting parser in french mode")
            cardsToAdd = self.csvparser.parse_fr(filesrc)
            
        if(self.language == 'it'):
            print("starting parser in italian mode")
            cardsToAdd = self.csvparser.parse_it(filesrc)
            
        if(self.language == 'tr'):
            print("starting parser in turkish mode")
            cardsToAdd = self.csvparser.parse_tr(filesrc)

        if(self.language == 'es'):
            print("starting parse in spanish mode")
            cardsToAdd = self.csvparser.parse_es(filesrc)
            
        if(self.language == 'ar'):
            print("starting parse in arabic mode")
            cardsToAdd = self.csvparser.parse_ar(filesrc)

        print("reading finished: {0} cards found".format(len(cardsToAdd)))
        
        return cardsToAdd