# -*- coding: utf-8 -*--

import argparse, json
from components.config.configmanager import ConfigManager
from components.ankiutil import AnkiUtil

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="ar/es/pl/fr/tr/it/ro/se/pt/uk")
parser.add_argument("-s", "--skipstore", help="skips store procedure")
parser.add_argument("-r", "--random", help="randomizes the import order")
parser.add_argument("-re", "--reshape", help="enable reshape mode (arabic)")
parser.add_argument("-p", "--phrase", help="sets the importer to phrase/sentence-mode")
parser.add_argument("-e", "--existing", help="enables check for existing cards - currently only compatible with active decks")
parser.add_argument("-params", "--params", help="prints existing parameters")

args = parser.parse_args()

if args.params == "y":
    print("\n\n-l (mand: ar/es/pl/fr/tr/it) = sets the language context\n-s (opt: y) = skips insert when true\n-r (opt: y) = inserts cards in random order when true\n")
    exit(1)

if args.language == None:
    print("no language set, returning...")
    exit(0)

phrase_mode = args.phrase == 'y'
skip_store = args.skipstore == 'y'
random = args.random == "y"
check_existing = args.existing == "y"
reshape = args.reshape == "y"

configmanager = None
with open ('.\components\config\config.json') as file:
        config = json.load(file)
        configmanager = ConfigManager(config, args.language, skip_store, random, check_existing, phrase_mode, reshape)
        
configmanager.print_config()

value = input("Continue? y/n\n")

if value == "y":
    ankiutil = AnkiUtil(configmanager)
    ankiutil.create_cards_from_file(phrase_mode) 