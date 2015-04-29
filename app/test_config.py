#!/usr/bin/env python

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('../TWITTER_API_KEYS')

print config.get('twitterapi', 'api_key')
print config.get('twitterapi', 'api_secret')
