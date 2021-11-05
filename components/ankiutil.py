# -*- coding: utf-8 -*-

import json
import re

from .ankiconnector import AnkiConnector
from .audiogenerator import AudioGenerator
from .jsonbuilder import JsonBuilder
from .csvparser import CSVParser

class AnkiUtil(object):
    
    def __init__(self, language, filedest, address):
        self.ankiconnector = AnkiConnector(address)
        self.audiogenerator = AudioGenerator(language, filedest)
        self.builder = JsonBuilder()
        self.csvparser = CSVParser(self.audiogenerator, self.builder)
        self.language = language
        
    def create_cards_from_file(self, filesrc, skip_store):
        
        cardsToAdd = self._read_cards_from_file(filesrc)
        if not cardsToAdd:
            print("error while reading the file: {0} with the language {1}".format(filesrc, self.language))
            return
            
        total = len(cardsToAdd)
        
        if skip_store:
            print("skipping insert of {0} cards".format(total))
            return
        
        counter = 1
        for card in cardsToAdd:
            print("inserting cards {0}/{1}".format(counter, total))
            response = self.ankiconnector.post(card)
            print(response.content)
            counter = counter + 1

    def add_audio_to_card_in_deck(self, query, skip_store):

        query_note_ids = self.builder.find_note_ids(query)
        response_note_ids = self.ankiconnector.post(query_note_ids)
        note_ids = json.loads(response_note_ids.content)["result"]


        query_note_info = self.builder.get_note_info(note_ids)
        response_note_info = self.ankiconnector.post(query_note_info)
        note_info = json.loads(response_note_info.content)["result"]

        clean_re = re.compile('<.*?>')

        counter = 1
        for each_info in note_info:
            print("adding audio to card: {}/{}".format(counter, len(note_info)))
            
            note_id = each_info["noteId"]
            word = each_info["fields"]["Front"]["value"]
            clean_word = re.sub(clean_re, '', word)

            print("note id: {} word: {}".format(note_id, clean_word))

            if skip_store:
                print("skipping audio insert of {0} cards".format(len(note_info)))
                return

            if counter == 2:
                break

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
            
        print("reading finished: {0} cards found".format(len(cardsToAdd)))
        
        return cardsToAdd