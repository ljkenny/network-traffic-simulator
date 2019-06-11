#!/usr/bin/python

import goslate
import random

from cb_utils import write_log

phrases = [ 'Hello, how are you today?',
            'Which way to the train station?',
            'It\'s nice to meet you.  Hopefully see you again soon.',
            'How much is the last cheese on the right?' ]
languages = ['de', 'es', 'sw', 'vi', 'fr']

AGENT_NAME = "TRANSLATE"

class TRANSLATE:
    def __init__(self):
        pass

    def translate(self):
        gs = goslate.Goslate()

        phrase = random.choice(phrases)
        language = random.choice(languages)

        write_log(AGENT_NAME, "Translating: \"%s\" from en to %s" % (phrase, language))
        write_log(AGENT_NAME, "Response: \"%s\"" % (gs.translate(phrase, language).encode('utf-8')))
