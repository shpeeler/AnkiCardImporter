# -*- coding: utf-8 -*--

import argparse
from components.cardcreator import CardCreator

# parse args
parser = argparse.ArgumentParser(description="Read Sentence")
parser.add_argument("-l", "--language", help="en/fr/es/it/pl")
parser.add_argument("-f", "--filesrc", help="source")
parser.add_argument("-d", "--filedest", help="destination")
parser.add_argument("-a", "--address", help="endpoint")
parser.add_argument("-s", "--skipstore", help="skips store procedure")

args = parser.parse_args()
skip_store = args.skipstore == 'y'

if skip_store:
    print("skip store set, cards wont be generated")

print("arguments parsed")

cardcreator = CardCreator(args.language, args.filedest, args.address)
cardcreator.create_cards_from_file(args.filesrc, skip_store)