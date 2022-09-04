# -*- coding: utf-8 -*--

import argparse, json
from components.config.configmanager import ConfigManager
from components.ankiutil import AnkiUtil

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="en/fr/es/it/pl/ro")
parser.add_argument("-s", "--skipstore", help="skips store procedure")
parser.add_argument("-f", "--force", help="forces new audio entries")
parser.add_argument("-p", "--plural", help="enable if plural is present")
parser.add_argument("-r", "--reshape", help="enable if arabic script is present")
parser.add_argument("-params", "--params", help="prints existing parameters")

args = parser.parse_args()

if args.params == "y":
    print("\n\n-l (mand: ar/es/pl/fr/tr/it) = sets the language context\n-s (opt: y) = skips insert when true\n-f (opt: y) = forces updates when true\n-p (opt: y) = inserts audio for plural when true\n-r (opt: y) = reshapes the word, only useful for rtl-languages\n")
    exit(1)

if args.language == None:
    print("no language set, returning...")
    exit(0)

skip_store = args.skipstore == 'y'
force = args.force == "y"
plural = args.plural == "y"
reshape = args.reshape == "y"

configmanager = None
with open ('.\components\config\config.json') as file:
        config = json.load(file)
        configmanager = ConfigManager(config, args.language, skip_store)

configmanager.print_config()

value = input("Continue? y/n\n")

if value == "y":
    ankiutil = AnkiUtil(configmanager)
    ankiutil.add_audio_to_card_in_deck(force, plural, reshape)