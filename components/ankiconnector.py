# -*- coding: utf-8 -*-

from .jsonbuilder import JsonBuilder
import requests

class AnkiConnector(object):
    
    def __init__(self, address):
        self.address = address
        
        
    def create_card(self, card_json):
        return requests.post(self.address, json = card_json)