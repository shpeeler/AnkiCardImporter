import json

class ConfigManager(object):

    Address = None
    FileDestination = None
    FileSource = None
    LanguageCode = None
    Language = None
    Deck = None
    SkipAudio = None
    DeckSentence = None
    Query = None
    QueryDeck = None
    QuerySuspended = None
    Reshape = False
    SkipStore = False
    RandomInsert = False
    CheckExisting = False
    SheetName = None

    def __init__(self, config_json, language, test = False, random = False, existing = False, phrase_mode = False, reshape = False, skip_audio = False):
        self.LanguageCode = language        
        self.Reshape = reshape
        self.SkipAudio = skip_audio
        self.Language = config_json["language_map"][language.lower()]
        self.Tld = config_json["tld"][language.lower()]
        self.Address = config_json["address"]

        if not phrase_mode:
            self.SheetName = config_json["sheet_name"]["Vocab"]
        else:
            self.SheetName = config_json["sheet_name"]["Sentence"]

        self.FileSource = config_json["file_source"][language.lower()]
        self.Query = config_json["query_repo"][language.lower()]
        self.QueryDeck = config_json["query_deck"][language.lower()]
        self.QuerySuspended = config_json["query_suspended"][language.lower()]
        self.Deck = config_json["deck_vocab"][language.lower()]
        self.DeckSentence = config_json["deck_sentence"][language.lower()]

        self.SkipStore = test
        self.RandomInsert = random
        self.CheckExisting = existing

        if test == False:
            self.FileDestination = config_json["file_destination"]
        else:
            self.FileDestination = config_json["file_destination_test"]

    def print_config(self):
        print("\nLanguage = {} ({})\nTLD = {}\nSheet = {}\nSkip-Store = {}\nRandom-Insert = {}\nCheckExisting = {}\nReshape = {}\nSkip-Audio = {}\nAddress = {}\nFile-Source = {}\nFile-Destination = {}\nQuery-Repository = {}\nQuery-Deck = {}\nDeck = {}\nDeck-Sentence = {}\n".format(self.Language, self.LanguageCode.upper(), self.Tld, self.SheetName, self.SkipStore, self.RandomInsert, self.CheckExisting, self.Reshape, self.SkipAudio, self.Address, self.FileSource, self.FileDestination, self.Query, self.QueryDeck, self.Deck, self.DeckSentence))