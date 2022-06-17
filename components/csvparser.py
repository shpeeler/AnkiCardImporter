# -*- coding: utf-8 -*-

import uuid, codecs
from .jsonbuilder import JsonBuilder
from .audiogenerator import AudioGenerator

class CSVParser(object):
    
    def __init__(self, generator, builder):
        self.builder = builder
        self.audiogenerator = generator
    
    def parse_ar(self, file):

        cardsToCreate = list()
        
        counter = 1

        first_line = True
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()
            while line:    
                values = line.split(';')
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue

                if len(values) == 6:
                    translation = values[0].strip()
                    gender = values[1].strip()
                    note = values[2].strip()
                    tags = values[3].strip()
                    word = values[4].strip()
                    plural = values[5].strip()
                    
                    print("Nr. {0} - parsing json for word: {1}".format(counter, word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_ar("Repository::Vocab::Arabic", "Vocab AR", note_id, gender, word, plural, translation, note, tagslist)
                    else:
                        json = self.builder.create_jsondict_ar("Repository::Vocab::Arabic", "Vocab AR", note_id, gender, word, plural, translation, note)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    counter = counter + 1
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate

    def parse_es(self, file):

        cardsToCreate = list()
        
        counter = 1

        first_line = True
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()
            while line:    
                values = line.split(';')
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue

                if len(values) == 5:
                    word = values[0].strip()
                    translation = values[1].strip()
                    gender = values[2].strip()
                    note = values[3].strip()
                    tags = values[4].strip()
                    
                    print("Nr. {0} - parsing json for word: {1}".format(counter, word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_es("Repository::Vocab::Spanish", "Vocab ES", note_id, gender, word, translation, note, tagslist)
                    else:
                        json = self.builder.create_jsondict_es("Repository::Vocab::Spanish", "Vocab ES", note_id, gender, word, translation, note)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    counter = counter + 1
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate



    def parse_pl(self, file):
        
        cardsToCreate = list()
        
        first_line = True
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()
            while line:    
                values = line.split(';')
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue

                if len(values) == 5:
                    word = values[0].strip()
                    translation = values[1].strip()
                    gender = values[2].strip()
                    note = values[3].strip()
                    tags = values[4].strip()
                    
                    print("parsing json for word: {0}".format(word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_pl("Repository::Vocab::Polish", "Vocab PL", note_id, gender, word, translation, note, tagslist)
                    else:
                        json = self.builder.create_jsondict_pl("Repository::Vocab::Polish", "Vocab PL", note_id, gender, word, translation, note)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate

    def parse_fr(self, file):
        
        cardsToCreate = list()
        
        first_line = True
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()
            while line:    
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue

                values = line.split(';')

                if len(values) == 6:
                    word = values[0].strip()
                    translation = values[1].strip()
                    gender = values[2].strip()
                    tags = values[3].strip()
                    definition = values[4].strip()
                    example = values[5].strip()
                    
                    print("parsing json for word: {0}".format(word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_fr("Repository::Vocab::French", "Vocab FR Base", note_id, gender, word, translation, definition, example, tagslist)
                    else:
                        json = self.builder.create_jsondict_fr("Repository::Vocab::French", "Vocab FR Base", note_id, gender, word, translation, definition, example)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate
    
    def parse_tr(self, file):
        
        cardsToCreate = list()
        first_line = True
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()
            while line:    
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue
                    
                values = line.split(';')

                if len(values) == 5:
                    word = values[0].strip()
                    translation = values[1].strip()
                    definition = values[2].strip()
                    example = values[3].strip()
                    tags = values[4].strip()
                    
                    print("parsing json for word: {0}".format(word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_tr("Repository::Vocab::Turkish", "Vocab TR", note_id, word, translation, definition, example, tagslist)
                    else:
                        json = self.builder.create_jsondict_tr("Repository::Vocab::Turkish", "Vocab TR", note_id, word, translation, definition, example)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate
    
    def parse_it(self, file):
        cardsToCreate = list()
        first_line = True
        
        with codecs.open(file, 'r', 'utf-8') as f:
            line = f.readline()[1:]
            while line:    
                values = line.split(';')
                if(first_line):
                    first_line = False
                    line = f.readline()
                    continue

                if len(values) == 5:
                    word = values[0].strip()
                    translation = values[1].strip()
                    gender = values[2].strip()
                    note = values[3].strip()
                    tags = values[4].strip()
                    
                    print("parsing json for word: {0}".format(word))
                    
                    note_id = uuid.uuid4()
                    
                    json = None
                    
                    if tags:
                        tagslist = tags.split(',')
                        json = self.builder.create_jsondict_it("Repository::Vocab::Italian", "Vocab IT", note_id, gender, word, translation, note, tagslist)
                    else:
                        json = self.builder.create_jsondict_it("Repository::Vocab::Italian", "Vocab IT", note_id, gender, word, translation, note)
                    
                    if json:
                        self.audiogenerator.speak(word)
                        cardsToCreate.append(json)
                    
                    line = f.readline()
                else:
                    print("invalid value count")
                    raise Exception()
        
        return cardsToCreate