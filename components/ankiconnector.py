# -*- coding: utf-8 -*-

from .jsonbuilder import JsonBuilder
import requests

class AnkiConnector(object):
    
    def __init__(self, address):
        self.address = address
        
        
    def post(self, json):
        return requests.post(self.address, json = json)