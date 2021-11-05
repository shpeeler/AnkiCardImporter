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
                                    "deckName": "Repository::Vocab::Polish",
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
                                    "deckName": "Repository::Vocab::Turkish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_fr(self, deck, card_type, note_id, gender, word, english, german, definition, example, tags = None):
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
                                    "Definition": definition,
                                    "Example": example
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Repository::Vocab::French",
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
                                    "deckName": "Repository::Vocab::Italian",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
     
    def find_cards_by_deck(self, query):

        resultDict = dict(
            {
                "action": "findNotes",
                "version": 6,
                "params": {
                    "query": query
                }
            }
        )

        return resultDict

    def add_audio_by_id(self, id, language, word):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format(language, word)

        resultDict = dict(
            {
                "action": "updateNoteFields",
                "version": 6,
                "params": {
                    "note": {
                        "id": str(id),
                        "fields": {
                            "Audio": audiofilename
                        }
                    }
                }
            }
        )

        return resultDict

    def _add_tags_to_jsondict(self, json, tags):
        
        if(tags != None):
            for tag in tags:
                json["params"]["note"]["tags"].append(tag)
                
        return json
        