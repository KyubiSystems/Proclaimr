#!/usr/bin/env python

# hello world example

import ConfigParser
import tweepy

config = ConfigParser.ConfigParser()
config.read('../TWITTER_API_KEYS')

consumer_key = config.get('twitterapi', 'api_key')
consumer_secret = config.get('twitterapi', 'api_secret')

access_token = config.get('twitterapi', 'access_token')
access_token_secret =  config.get('twitterapi', 'access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline('Rocketeer_UK')
for tweet in public_tweets:

    print tweet.id
    print tweet.text
    try:
        print '@' + tweet.entities['user_mentions'][0]['screen_name'] + '  (' + tweet.entities['user_mentions'][0]['name'] + ')'
    except:
        print 'Mention not found'

    print tweet.created_at
    print tweet.retweeted
    print '---------------------------------------'
