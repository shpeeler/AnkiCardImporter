# -*- coding: utf-8 -*--

import argparse
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
skip_store = args.skipstore == 'y'
force = args.force == "y"
plural = args.plural == "y"
reshape = args.reshape == "y"

if skip_store:
    print("skip store set, cards wont be generated")

print("arguments parsed")

ankiutil = AnkiUtil(args.language, args.filedest, args.address)

ankiutil.add_audio_to_card_in_deck(args.query, skip_store, force, plural, reshape)