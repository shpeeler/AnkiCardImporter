import argparse, json
from components.config.configmanager import ConfigManager
from components.ankiutil import AnkiUtil

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="en/fr/es/it/pl/ro")
parser.add_argument("-s", "--skipstore", help="skips store procedure")
parser.add_argument("-params", "--params", help="prints existing parameters")

args = parser.parse_args()

if args.params == "y":
    print("\n\n-l (mand: ar/es/pl/fr/tr/it) = sets the language context\n-s (opt: y) = skips insert when true")
    exit(1)

if args.language == None:
    print("no language set, returning...")
    exit(0)

skip_store = args.skipstore == 'y'

configmanager = None
with open ('.\components\config\config.json') as file:
        config = json.load(file)
        configmanager = ConfigManager(config, args.language, skip_store)

configmanager.print_config()

value = input("Continue? y/n\n")

if value == "y":
    ankiutil = AnkiUtil(configmanager)
    ankiutil.clean_card()