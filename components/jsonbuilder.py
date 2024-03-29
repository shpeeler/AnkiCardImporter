# -*- coding: utf-8 -*-

class JsonBuilder(object):

    def __init__(self):
        pass
    
    def create_jsondict_sentence(self, deck, card_type, language, note_id, sentence, translation, note, tags, skip_audio):

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

        if tags != None and tags != "":
            resultDict = self._add_tags_to_jsondict(resultDict, tags)
                        
        return resultDict

    def create_jsondict_word(self, deck, card_type, language, note_id, word, translation, word_pl, gender, tags, note, example, skip_audio = False):

        audio = ""
        audio_pl = ""
        
        if skip_audio == False:
            audio = "[sound:audio_{0}_{1}.mp3]".format(language, str(note_id))
            
            if word_pl != None and word_pl != "" and word_pl != "ø":
                audio_pl = "[sound:audio_{0}_{1}_plural.mp3]".format(language, str(note_id))

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
                                    "Word Plural": word_pl,
                                    "Translation": translation,
                                    "Gender": gender,
                                    "Example": example,
                                    "Note": note,
                                    "Audio": audio,
                                    "Audio Plural": audio_pl
                                },
                            "tags": []
                            }
                        }
                    })

        if tags != None and tags != "":
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

    def add_audio_by_id(self, id, language, audio_name):

        audiofilename = "[sound:audio_{0}_{1}.mp3]".format(language, audio_name)

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

    def update_name(self, id, new_name):

        resultDict = dict(
            {
                "action": "updateNoteFields",
                "version": 6,
                "params": {
                    "note": {
                        "id": id,
                        "fields": {
                            "Word": new_name
                        }
                    }
                }
            }
        )

        return resultDict

    def add_audio_by_id_plural(self, id, language, audio_name):

        audiofilename = "[sound:audio_{0}_{1}_plural.mp3]".format(language, audio_name)

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
        