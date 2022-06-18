# -*- coding: utf-8 -*-

import argparse, json
from gtts import gTTS

class AudioGenerator(object):
    
    def __init__(self, language, destination_path):
        self.language = language
        self.destination_path = destination_path

    def speak(self, sentence, filename = None):
        tts = gTTS(sentence, lang=self.language)

        final_filename = None
        if filename != None:
            final_filename = filename
        else:
            final_filename = sentence.replace("?", "")

        tts.save("{0}\\audio_{1}_{2}.mp3".format(self.destination_path, self.language, final_filename))