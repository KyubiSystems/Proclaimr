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

# Set up Twython object, using OAuth2
twitter = Twython(api_key, api_secret, oauth_version=2)
access_token = twitter.obtain_access_token()

twitter = Twython(api_key, access_token=access_token)

user_timeline = twitter.get_user_timeline(screen_name='NASA')

# Mon Nov 30 20:12:01 +0000 2015
for tweet in user_timeline:
    print(tweet['text'])
    dt = parser.parse(tweet['created_at'])
    print dt
    a = arrow.get(dt)
    print a.humanize()
    
    print(tweet['user']['name'])
    print(tweet['user']['description'])
    try:
        media = tweet['entities']['media']
    except KeyError:
        media = ''
    print media
    print
