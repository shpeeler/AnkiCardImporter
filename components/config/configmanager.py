import json

class ConfigManager(object):

    Address = None
    FileDestination = None
    FileSource = None
    LanguageCode = None
    Language = None
    Query = None
    SkipStore = False
    RandomInsert = False

    def __init__(self, config_json, language, test = False, random = False):
        self.LanguageCode = language
        self.Language = config_json["language_map"][language.lower()]
        self.Address = config_json["address"]
        self.FileSource = config_json["file_source"][language.lower()]
        self.Query = config_json["query"][language.lower()]
        self.SkipStore = test
        self.RandomInsert = random

        if test == False:
            self.FileDestination = config_json["file_destination"]
        else:
            self.FileDestination = config_json["file_destination_test"]

    def print_config(self):
        print("\nLanguage = {} ({})\nSkip-Store = {}\nRandom-Insert = {}\nAddress = {}\nFile-Source = {}\nFile-Destination = {}\nQuery = {}\n".format(self.Language, self.LanguageCode.upper(), self.SkipStore, self.RandomInsert, self.Address, self.FileSource, self.FileDestination, self.Query))