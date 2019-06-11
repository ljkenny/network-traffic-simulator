import tweepy
import random
import time
import sys
import os

from cb_utils import write_log, write_debug, get_dir_path

AGENT_NAME = "SOCIAL"

# Enter the corresponding information from your Twitter Application
# For twitter account twit_2_woo
CONSUMER_KEY = '<###KEY###>'
CONSUMER_SECRET = '<###SECRET###>'
ACCESS_KEY = '<###KEY###>'
ACCESS_SECRET = '<###SECRET###>'

tweets = [ 'Hello World',
           'What big eyes you have :0' ]

class TWITTER:
    def __init__(self):
        pass

    def post(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        dir_path = get_dir_path()

        tweet = random.choice(tweets)
        rand = random.getrandbits(8)

        try:
            post = "[%s] %s" %(rand, tweet)
            rc = api.update_status(status=post)
            write_log(AGENT_NAME, "Tweeting \"%s\"" % (post))
        except:
            write_log(AGENT_NAME, "Failed to tweet\"%s\"" % post)
