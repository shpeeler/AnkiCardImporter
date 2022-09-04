import json

class ConfigManager(object):

    Address = None
    FileDestination = None
    FileSource = None
    LanguageCode = None
    Language = None
    Query = None
    QueryDeck = None
    SkipStore = False
    RandomInsert = False
    CheckExisting = False

    def __init__(self, config_json, language, test = False, random = False, existing = False):
        self.LanguageCode = language
        self.Language = config_json["language_map"][language.lower()]
        self.Address = config_json["address"]
        self.FileSource = config_json["file_source"][language.lower()]
        self.Query = config_json["query_repo"][language.lower()]
        self.QueryDeck = config_json["query_deck"][language.lower()]
        self.SkipStore = test
        self.RandomInsert = random
        self.CheckExisting = existing

        if test == False:
            self.FileDestination = config_json["file_destination"]
        else:
            self.FileDestination = config_json["file_destination_test"]

    def print_config(self):
        print("\nLanguage = {} ({})\nSkip-Store = {}\nRandom-Insert = {}\nCheckExisting = {}\nAddress = {}\nFile-Source = {}\nFile-Destination = {}\nQuery-Repository = {}\nQuery-Deck = {}\n".format(self.Language, self.LanguageCode.upper(), self.SkipStore, self.RandomInsert, self.CheckExisting, self.Address, self.FileSource, self.FileDestination, self.Query, self.QueryDeck))