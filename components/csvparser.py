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
                        
                        if word_pl != None:
                            self.audiogenerator.speak(word_pl)  

                        cardsToCreate.append(json)

                else:
                    message = "invalid value count: {0}".format(len(values))
                    print(message)
                    raise Exception(message)


                counter = counter + 1
        
        return cardsToCreate

    def parse(self, file, language):

        cardsToCreate = list()
        counter = 1

        with codecs.open(file, 'r', 'utf-8') as f:
            lines = f.readlines()[1:]
            line_count = len(lines)

            for line in lines:
                values = line.split(';')

                print("{}/{} parsing...".format(counter, line_count))

                card = None
                if(language == 'ar'):
                    card = self.parse_ar(values)

                if(language == 'pl'):
                    card = self.parse_pl(values)
                    
                if(language == 'fr'):
                    card = self.parse_fr(values)
                    
                if(language == 'it'):
                    card = self.parse_it(values)
                    
                if(language == 'tr'):
                    card = self.parse_tr(values)

                if(language == 'es'):
                    card = self.parse_es(values)

                if card != None:
                    cardsToCreate.append(card)
                    
                counter = counter + 1

        return cardsToCreate

    def parse_ar(self, values):

        result = None
        if len(values) == 7:
            translation = values[0].strip()
            gender = values[1].strip()
            note = values[2].strip()
            tags = values[3].strip()
            pronunciation = values[4].strip()
            word = values[5].strip()
            plural = values[6].strip()

            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None
            
            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_ar("Backlog::Vocab::Arabic", "Vocab AR", note_id, gender, word, plural, pronunciation, translation, note, tagslist)
            else:
                json = self.builder.create_jsondict_ar("Backlog::Vocab::Arabic", "Vocab AR", note_id, gender, word, plural, pronunciation, translation, note)
            
            if json:
                self.audiogenerator.speak(word)

                if plural != "" and plural != None:
                    self.audiogenerator.speak(plural)
                    
                result = json

        else:
            print("invalid value count: {0}".format(len(values)))
            raise Exception()

        return result

    def parse_es(self, values):

        result = None
        if len(values) == 5:
            word = values[0].strip()
            translation = values[1].strip()
            gender = values[2].strip()
            note = values[3].strip()
            tags = values[4].strip()
            
            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None
            
            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_es("Repository::Vocab::Spanish", "Vocab ES", note_id, gender, word, translation, note, tagslist)
            else:
                json = self.builder.create_jsondict_es("Repository::Vocab::Spanish", "Vocab ES", note_id, gender, word, translation, note)
            
            if json:
                self.audiogenerator.speak(word)
                result = json
            
        else:
            print("invalid value count")
            raise Exception()

        return result
        
    def parse_pl(self, values):
        
        result = None
        if len(values) == 5:
            word = values[0].strip()
            translation = values[1].strip()
            gender = values[2].strip()
            note = values[3].strip()
            tags = values[4].strip()
            
            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None

            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_pl("Repository::Vocab::Polish", "Vocab PL", note_id, gender, word, translation, note, tagslist)
            else:
                json = self.builder.create_jsondict_pl("Repository::Vocab::Polish", "Vocab PL", note_id, gender, word, translation, note)
            
            if json:
                self.audiogenerator.speak(word)
                result = json
            
        else:
            print("invalid value count")
            raise Exception()
        
        return result

    def parse_fr(self, values):
        
        result = None
        if len(values) == 6:
            word = values[0].strip()
            translation = values[1].strip()
            gender = values[2].strip()
            tags = values[3].strip()
            definition = values[4].strip()
            example = values[5].strip()
            
            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None
            
            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_fr("Repository::Vocab::French", "Vocab FR Base", note_id, gender, word, translation, definition, example, tagslist)
            else:
                json = self.builder.create_jsondict_fr("Repository::Vocab::French", "Vocab FR Base", note_id, gender, word, translation, definition, example)

            if json:
                self.audiogenerator.speak(word)
                result = json
            
        else:
            print("invalid value count")
            raise Exception()
        
        return result
    
    def parse_tr(self, values):
        
        result = None
        if len(values) == 5:
            word = values[0].strip()
            translation = values[1].strip()
            definition = values[2].strip()
            example = values[3].strip()
            tags = values[4].strip()
            
            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None
            
            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_tr("Repository::Vocab::Turkish", "Vocab TR", note_id, word, translation, definition, example, tagslist)
            else:
                json = self.builder.create_jsondict_tr("Repository::Vocab::Turkish", "Vocab TR", note_id, word, translation, definition, example)
            
            if json:
                self.audiogenerator.speak(word)
                result = json
        else:
            print("invalid value count")
            raise Exception()
        
        return result
    
    def parse_it(self, values):
        
        result = None
        if len(values) == 5:
            word = values[0].strip()
            translation = values[1].strip()
            gender = values[2].strip()
            note = values[3].strip()
            tags = values[4].strip()
            
            note_id = uuid.uuid4()
            
            if self.existing_cards != None and word in self.existing_cards:
                print("card {0} exists already".format(word))
                return None

            json = None
            
            if tags:
                tagslist = tags.split(',')
                json = self.builder.create_jsondict_it("Repository::Vocab::Italian", "Vocab IT", note_id, gender, word, translation, note, tagslist)
            else:
                json = self.builder.create_jsondict_it("Repository::Vocab::Italian", "Vocab IT", note_id, gender, word, translation, note)
            
            if json:
                self.audiogenerator.speak(word)
                result = json
            
        else:
            print("invalid value count")
            raise Exception()
        
        return result