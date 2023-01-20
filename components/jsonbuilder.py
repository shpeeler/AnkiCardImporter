# -*- coding: utf-8 -*-

class JsonBuilder(object):
    
    def __init__(self):
        pass
    
    def create_jsondict_sentence(self, deck, card_type, language, note_id, sentence, translation, note):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format(language, note_id)

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
                                    "Sentence": sentence,
                                    "Translation": translation,
                                    "Note": note,
                                    "Audio": audiofilename,
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": deck,
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
                        
        return resultDict

    def create_jsondict_ar(self, deck, card_type, note_id, gender, word, plural, pronunciation, translation, note, tags = None):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("ar", word)

        audiofilename_plural = ""
        if plural != "" and plural != None:
            audiofilename_plural = "[sound:audio_{0}_{1}.mp3]".format("ar", plural)
        
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
                                    "Plural": plural,
                                    "Pronunciation": pronunciation,
                                    "Translation": translation,
                                    "Note": note,
                                    "Audio": audiofilename,
                                    "Audio Plural": audiofilename_plural
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Backlog::Vocab::Arabic",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict

    def create_jsondict_es(self, deck, card_type, note_id, gender, word, translation, note, tags = None):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format("es", word)
        
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
                                    "Translation": translation,
                                    "Note": note,
                                    "Audio": audiofilename
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Backlog::Vocab::Spanish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict

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
                                    "deckName": "Backlog::Vocab::Polish",
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
                                    "deckName": "Backlog::Vocab::Turkish",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_fr(self, deck, card_type, note_id, gender, word, translation, definition, example, tags = None):
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
                                    "Word": word,
                                    "Translation": translation,
                                    "Audio": audiofilename,
                                    "Definition": definition,
                                    "Example": example
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Backlog::Vocab::French",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
    
    def create_jsondict_it(self, deck, card_type, note_id, gender, word, translation, note, tags = None):
        
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
                                    "Word": word,
                                    "Translation": translation,
                                    "Note": note,
                                    "Audio": audiofilename,
                                },
                            "options": {
                                "allowDuplicate": False,
                                "duplicateScope": "deck",
                                "duplicateScopeOptions": {
                                    "deckName": "Backlog::Vocab::Italian",
                                    "checkChildren": False
                                }
                                },
                            "tags": []
                            }
                        }
                    })
        
        resultDict = self._add_tags_to_jsondict(resultDict, tags)
                
        return resultDict
     
    def find_note_ids(self, query):

        resultDict = dict(
            {
                "action": "findNotes",
                "version": 6,
                "params": {
                    "query": str(query)
                }
            }
        )

        return resultDict

    def get_note_info(self, ids):

        resultDict = dict(
            {
                "action": "notesInfo",
                "version": 6,
                "params": {
                    "notes": ids
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
                        "id": id,
                        "fields": {
                            "Audio": audiofilename
                        }
                    }
                }
            }
        )

        return resultDict

    def add_audio_by_id_plural(self, id, language, word):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format(language, word)

        resultDict = dict(
            {
                "action": "updateNoteFields",
                "version": 6,
                "params": {
                    "note": {
                        "id": id,
                        "fields": {
                            "Audio Plural": audiofilename
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
        