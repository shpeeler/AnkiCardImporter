# -*- coding: utf-8 -*-

import argparse, json, requests
from gtts import gTTS

class AudioGenerator(object):
    
    def __init__(self, language, destination_path, tld = None):
        self.language = language
        self.destination_path = destination_path
        self.tld = tld

    def speak(self, sentence, filename = None):
        
        if self.tld != "" and self.tld != None:
            tts = gTTS(sentence, lang=self.language, tld=self.tld)
        else:
            tts = gTTS(sentence, lang=self.language)

        final_filename = None
        if filename != None:
            final_filename = filename
        else:
            final_filename = sentence.replace("?", "")

        try:
            tts.save("{0}\\audio_{1}_{2}.mp3".format(self.destination_path, self.language, final_filename))
        except Exception as e:
            print("unable to generate audio files: {0}".format(e))
            return False
        
        return True