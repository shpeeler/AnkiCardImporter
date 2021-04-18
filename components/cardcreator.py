# -*- coding: utf-8 -*-

from .ankiconnector import AnkiConnector
from .audiogenerator import AudioGenerator
from .csvparser import CSVParser

class CardCreator(object):
    
    def __init__(self, language, filedest, address):
        self.ankiconnector = AnkiConnector(address)
        self.audiogenerator = AudioGenerator(language, filedest)
        self.csvparser = CSVParser(self.audiogenerator)
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