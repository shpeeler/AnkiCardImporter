# -*- coding: utf-8 -*-

import uuid, codecs
import pandas as pd
from .jsonbuilder import JsonBuilder
from .audiogenerator import AudioGenerator

class XMLParser(object):
    
    def __init__(self, generator, builder, existing_cards):
        self.builder = builder
        self.audiogenerator = generator
        self.existing_cards = existing_cards
    
    def parse_sentence(self, file, sheet, language, deck):

        cardsToCreate = list()
        counter = 1

        data = pd.read_excel(file, sheet)
        total = len(data.index)

        for each in data.itertuples():
            sentence = each[1]
            translation = each[2]
            note = each[3]

            if note != note:
                note = ""

            note_id = uuid.uuid4()

            print("parsing: {0}/{1} - {2} => {3}".format(counter, total, sentence, translation))

            json = self.builder.create_jsondict_sentence(deck, "Sentences", language, note_id, sentence, translation, note)
            if json:
                self.audiogenerator.speak(sentence, note_id)                        
                cardsToCreate.append(json)

            counter = counter + 1

        return cardsToCreate

    def parse_word(self, file, sheet, language, deck):
        cardsToCreate = list()
        counter = 1

        data = pd.read_excel(file, sheet)
        total = len(data.index)

        for each in data.itertuples():
            word        = values[1]
            word_pl     = values[2]
            translation = values[3]
            gender      = values[4]
            tags        = values[5]
            note        = values[6]
            example     = values[7]

            note_id = uuid.uuid4()

            print("parsing: {0}/{1} - {2} => {3}".format(counter, total, word, translation))

            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                continue

            json = self.builder.create_jsondict_word(deck, "Vocab", language, note_id, word, translation, word_pl, gender, tags, note, example)

            if json:
                self.audiogenerator.speak(word)                        
                
                if word_pl != None and word_pl != "" and word_pl != "ø":
                    self.audiogenerator.speak(word_pl)  

                cardsToCreate.append(json)

            counter = counter + 1
        
        return cardsToCreate