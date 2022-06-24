# -*- coding: utf-8 -*--

import argparse, json
from components.config.configmanager import ConfigManager
from components.ankiutil import AnkiUtil

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="en/fr/es/it/pl/ro")
parser.add_argument("-d", "--filedest", help="destination")
parser.add_argument("-q", "--query", help="specifies to which cards the audio is added")
parser.add_argument("-a", "--address", help="endpoint")
parser.add_argument("-s", "--skipstore", help="skips store procedure")
parser.add_argument("-f", "--force", help="forces new audio entries")
parser.add_argument("-p", "--plural", help="enable if plural is present")
parser.add_argument("-r", "--reshape", help="enable if arabic script is present")

args = parser.parse_args()

if args.language == None:
    print("no language set, returning...")
    exit(0)

skip_store = args.skipstore == 'y'
force = args.force == "y"
plural = args.plural == "y"
reshape = args.reshape == "y"

configmanager = None
with open ('.\config.json') as file:
        config = json.load(file)
        configmanager = ConfigManager(config, args.language, skip_store)

configmanager.print_config()

value = input("Continue? y/n\n")

if value == "y":
    ankiutil = AnkiUtil(configmanager)
    ankiutil.add_audio_to_card_in_deck(force, plural, reshape)