import json

class ConfigManager(object):

    Address = None
    FileDestination = None
    FileSource = None
    LanguageCode = None
    Language = None
    Deck = None
    Query = None
    QueryDeck = None
    SkipStore = False
    RandomInsert = False
    CheckExisting = False

    def __init__(self, config_json, language, test = False, random = False, existing = False, phrase_mode = False):
        self.LanguageCode = language
        self.Language = config_json["language_map"][language.lower()]
        self.Address = config_json["address"]
        
        if phrase_mode:
            self.FileSource = config_json["file_source_sentence"][language.lower()]
        else:
            self.FileSource = config_json["file_source"][language.lower()]

        if phrase_mode:
            self.Query = config_json["query_repo_sentence"][language.lower()]
        else:
            self.Query = config_json["query_repo"][language.lower()]

        if phrase_mode:
            self.QueryDeck = config_json["query_deck_sentence"][language.lower()]
        else:
            self.QueryDeck = config_json["query_deck"][language.lower()]
            
        self.Deck = config_json["deck"][language.lower()]
        self.SkipStore = test
        self.RandomInsert = random
        self.CheckExisting = existing

        if test == False:
            self.FileDestination = config_json["file_destination"]
        else:
            self.FileDestination = config_json["file_destination_test"]

    def print_config(self):
        print("\nLanguage = {} ({})\nSkip-Store = {}\nRandom-Insert = {}\nCheckExisting = {}\nAddress = {}\nFile-Source = {}\nFile-Destination = {}\nQuery-Repository = {}\nQuery-Deck = {}\n".format(self.Language, self.LanguageCode.upper(), self.SkipStore, self.RandomInsert, self.CheckExisting, self.Address, self.FileSource, self.FileDestination, self.Query, self.QueryDeck))