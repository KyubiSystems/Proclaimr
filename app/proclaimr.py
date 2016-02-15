#!/usr/bin/env python

import ConfigParser
import arrow

from dateutil import parser
from twython import Twython

from flask import Flask
app = Flask(__name__)

# Read API keys from config file
config = ConfigParser.ConfigParser()
config.read('../TWITTER_API_KEYS')
api_key = config.get('twitterapi', 'api_key')
api_secret = config.get('twitterapi', 'api_secret')

# Set up Twython object, using OAuth2
twitter = Twython(api_key, api_secret, oauth_version=2)
access_token = twitter.obtain_access_token()

twitter = Twython(api_key, access_token=access_token)
user_timeline = twitter.get_user_timeline(screen_name='NASA')

# Test user @NASA

@app.route("/")
def display():
    for tweet in user_timeline:

        r = tweet['text']
        dt = parser.parse(tweet['created_at'])
        r = r + str(dt)
        a = arrow.get(dt)
        r = r + a.humanize()
        
        #print(tweet['user']['name'])
        #print(tweet['user']['description'])
        try:
            media = tweet['entities']['media']
        except KeyError:
            media = ''

        r = r + str(media)
        return r
            
if __name__ == "__main__":
    app.run(port=5005, debug=True)
