#!/usr/bin/env python

import configparser
import arrow

from dateutil import parser
from twython import Twython

from flask import Flask
app = Flask(__name__)

# Read API keys from config file
config = configparser.ConfigParser()
config.read('../TWITTER_API_KEYS')
api_key = config.get('twitterapi', 'api_key')
api_secret = config.get('twitterapi', 'api_secret')

# Set up Twython object, using OAuth2
twitter = Twython(api_key, api_secret, oauth_version=2)
access_token = twitter.obtain_access_token()

twitter = Twython(api_key, access_token=access_token)
username = 'NASA'
user_timeline = twitter.get_user_timeline(screen_name=username)

# Test user @NASA

@app.route("/")
def display():
    r = '<ul>'
    for tweet in user_timeline:

        r = r + '<li>' + tweet['text']
        dt = parser.parse(tweet['created_at'])
        r = r + str(dt)
        a = arrow.get(dt)
        r = r + ' ' + a.humanize()
        
        #print(tweet['user']['name'])
        #print(tweet['user']['description'])
        try:
            media = tweet['entities']['media'][0]['media_url_https'] + ':orig'
        except KeyError:
            media = ''

        r = r + '<br/><img src="' + str(media) + '"><br/><br/>'

    r = r + '</ul>'
    
    return r
            
if __name__ == "__main__":

    print('Starting Proclaimr process on localhost:5005...')
    app.run(port=5005, debug=True)
