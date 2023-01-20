# -*- coding: utf-8 -*-

import uuid, codecs
from .jsonbuilder import JsonBuilder
from .audiogenerator import AudioGenerator

class CSVParser(object):
    
    def __init__(self, generator, builder, existing_cards):
        self.builder = builder
        self.audiogenerator = generator
        self.existing_cards = existing_cards
    
    def parse_sentence(self, file, language, deck):

        cardsToCreate = list()
        counter = 1

        with codecs.open(file, 'r', 'utf-8') as f:
            lines = f.readlines()[1:]
            line_count = len(lines)

            print("{}/{} parsing...".format(counter, line_count))

            for line in lines:
                values = line.split(';')

                print("{}/{} parsing...".format(counter, line_count))

                if len(values) == 3:
                    sentence = values[0].strip()
                    translation = values[1].strip()
                    note = values[2].strip()

                    note_id = uuid.uuid4()
                    
                    json = self.builder.create_jsondict_sentence(deck, "Sentences", language, note_id, sentence, translation, note)

                    if json:
                        self.audiogenerator.speak(sentence, note_id)                        
                        cardsToCreate.append(json)

                else:
                    print("invalid value count: {0}".format(len(values)))
                    raise Exception()

                counter = counter + 1

        return cardsToCreate

    def parse_word(self, file, language, deck):
        cardsToCreate = list()
        counter = 1

        with codecs.open(file, 'r', 'utf-8') as f:
            lines = f.readlines()[1:]
            line_count = len(lines)

            for line in lines:
                values = line.split(';')

                print("{}/{} parsing...".format(counter, line_count))

                if len(values) == 8:
                    word = values[0]
                    translation = values[1]
                    word_pl = values[2]
                    translation_pl = values[3]
                    gender = values[4]
                    tags = values[5]
                    note = values[6]
                    example = values[7]

                    note_id = uuid.uuid4()

                    if self.existing_cards != None and word in self.existing_cards:
                        print("card {0} exists already".format(word))
                        continue

                    json = self.builder.create_jsondict_word(deck, "Word", language, note_id, word, translation, word_pl, translation_pl, gender, tags, note, example)

                    if json:
                        self.audiogenerator.speak(word)                        
                        
                        if word_pl != None and word_pl != "":
                            self.audiogenerator.speak(word_pl)  

                        cardsToCreate.append(json)

                else:
                    message = "invalid value count: {0}".format(len(values))
                    print(message)
                    raise Exception(message)


                counter = counter + 1
        
        return cardsToCreate