#!/usr/bin/env python

import ConfigParser
import arrow
from dateutil import parser

from twython import Twython

config = ConfigParser.ConfigParser()
config.read('../TWITTER_API_KEYS')

# Read API keys from config file
api_key = config.get('twitterapi', 'api_key')
api_secret = config.get('twitterapi', 'api_secret')

access_token = config.get('twitterapi', 'access_token')
access_token_secret = config.get('twitterapi', 'access_token_secret')

# Set up Twython object
twitter = Twython(api_key, api_secret, access_token, access_token_secret)

user_timeline = twitter.get_user_timeline(screen_name='NASA')

# Mon Nov 30 20:12:01 +0000 2015
for tweet in user_timeline:
    print(tweet['text'])
    print(tweet['created_at'])
    dt = parser.parse(tweet['created_at'])
    print dt

    print(tweet['user']['name'])
    print(tweet['user']['description'])
    print

