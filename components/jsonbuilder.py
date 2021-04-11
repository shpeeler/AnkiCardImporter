# -*- coding: utf-8 -*-

class JsonBuilder(object):
    
    def __init__(self):
        pass
    
    def create_jsondict_pl(self, deck, card_type, note_id, gender, word, translation, note, tags = None):
        
        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("pl", word)
        
        resultDict = dict( 
                    {
                    "action": "addNote",
                    "version": 6,
                    "params": {
                        "note": {
                                "deckName": deck,
                                "modelName": card_type,
                                "fields": {
                                    "Note ID": str(note_id),
                                    "Gender": gender,
                                    "Word": word,
                                    "German": translation,
                                    "Note": note,
                                    "Audio": audiofilename
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Repository::CustomVocab::Polish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_tr(self, deck, card_type, note_id, word, translation, definition, example, tags = None):
        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("tr", word)
        
        resultDict = dict( 
                    {
                    "action": "addNote",
                    "version": 6,
                    "params": {
                        "note": {
                                "deckName": deck,
                                "modelName": card_type,
                                "fields": {
                                    "Note ID": str(note_id),
                                    "Word": word,
                                    "Translation": translation,
                                    "Definition": definition,
                                    "Example": example,
                                    "Audio": audiofilename,
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Repository::CustomVocab::Polish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_fr(self, deck, card_type, note_id, gender, word, english, german, tags = None):
        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("fr", word)
        
        resultDict = dict( 
                    {
                    "action": "addNote",
                    "version": 6,
                    "params": {
                        "note": {
                                "deckName": deck,
                                "modelName": card_type,
                                "fields": {
                                    "Note ID": str(note_id),
                                    "Gender": gender,
                                    "French": word,
                                    "English": english,
                                    "German": german,
                                    "Audio": audiofilename,
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Repository::CustomVocab::Polish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_it(self, deck, card_type, note_id, gender, word, french, english, german, tags = None):
        
        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("it", word)
        
        resultDict = dict( 
                    {
                    "action": "addNote",
                    "version": 6,
                    "params": {
                        "note": {
                                "deckName": deck,
                                "modelName": card_type,
                                "fields": {
                                    "Note ID": str(note_id),
                                    "Gender": gender,
                                    "Italian": word,
                                    "French": french,
                                    "English": english,
                                    "German": german,
                                    "Audio": audiofilename,
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Repository::CustomVocab::Polish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
     
    def _add_tags_to_jsondict(self, json, tags):
        
        if(tags != None):
            for tag in tags:
                json["params"]["note"]["tags"].append(tag)
                
        return json
        