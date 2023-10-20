# -*- coding: utf-8 -*-

import uuid, codecs
import pandas as pd
import arabic_reshaper

from bidi.algorithm import get_display
from .jsonbuilder import JsonBuilder
from .audiogenerator import AudioGenerator

class XMLParser(object):
    
    def __init__(self, generator, builder, existing_cards):
        self.builder = builder
        self.audiogenerator = generator
        self.existing_cards = existing_cards
    
    def parse_sentence(self, file, sheet, language, deck, reshape):

        cardsToCreate = list()
        counter = 1

        data = pd.read_excel(file, sheet)
        total = len(data.index)

        for each in data.itertuples():
            index       = self.empty_if_nan(each[0])
            sentence    = self.empty_if_nan(each[1])
            translation = self.empty_if_nan(each[2])
            note        = self.empty_if_nan(each[3])
            tags        = self.empty_if_nan(each[4])

            note_id = uuid.uuid4()

            if tags != "":
                tags = tags.split(',')
            
            print_sentence = sentence
            if reshape == True:
                reshaped_sentence = arabic_reshaper.reshape(sentence)
                print_sentence = get_display(reshaped_sentence)

            print("parsing: {0}/{1} - {2} => {3}".format(counter, total, print_sentence, translation))

            json = self.builder.create_jsondict_sentence(deck, "Sentences", language, note_id, sentence, translation, note, tags)
            if json:
                self.audiogenerator.speak(sentence, note_id)                        
                cardsToCreate.append(json)

            counter = counter + 1

        return cardsToCreate

    def parse_word(self, file, sheet, language, deck, reshape, skip_audio = False):
        cardsToCreate = list()
        counter = 1

        data = pd.read_excel(file, sheet)
        total = len(data.index)

        for each in data.itertuples():

            index       = self.empty_if_nan(each[0])
            word        = self.empty_if_nan(each[1])
            word_pl     = self.empty_if_nan(each[2])
            translation = self.empty_if_nan(each[3])
            gender      = self.empty_if_nan(each[4])
            tags        = self.empty_if_nan(each[5])
            note        = self.empty_if_nan(each[6])
            example     = self.empty_if_nan(each[7])

            note_id = uuid.uuid4()

            print_word = word
            if reshape == True:
                reshaped_word = arabic_reshaper.reshape(word)
                print_word = get_display(reshaped_word)

            if tags != "":
                tags = tags.split(',')

            print("parsing: {0}/{1} - {2} => {3}".format(counter, total, print_word, translation))

            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(print_word))
                continue

            json = self.builder.create_jsondict_word(deck, "Vocab", language, note_id, word, translation, word_pl, gender, tags, note, example, skip_audio)

            if json:
                if skip_audio == False:
                    if self.audiogenerator.speak(word, str(note_id)) == False:
                        print("error during audio generation for card '{}' - returning the processed cards".format(word))
                        return                     
                    
                    if word_pl != "" and word_pl != "ø":

                        if self.audiogenerator.speak(word_pl, str(note_id) + "_plural") == False:
                            print("error during audio generation for card '{}' - returning the processed cards".format(word_pl))
                            return  
                
                cardsToCreate.append(json)

            counter = counter + 1
        
        return cardsToCreate


    def empty_if_nan(self, value):

        if value != value or value == None:
            return ""

        return value