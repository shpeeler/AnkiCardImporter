# -*- coding: utf-8 -*--

import argparse, json
from components.config.configmanager import ConfigManager
from components.ankiutil import AnkiUtil

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="ar/es/pl/fr/tr/it")
parser.add_argument("-s", "--skipstore", help="skips store procedure")
parser.add_argument("-r", "--random", help="randomizes the import order")

args = parser.parse_args()

if args.language == None:
    print("no language set, returning...")
    exit(0)

skip_store = args.skipstore == 'y'
random = args.random == "y"

configmanager = None
with open ('.\config.json') as file:
        config = json.load(file)
        configmanager = ConfigManager(config, args.language, skip_store, random)
        
configmanager.print_config()

value = input("Continue? y/n\n")

if value == "y":
    ankiutil = AnkiUtil(configmanager)
    ankiutil.create_cards_from_file() 