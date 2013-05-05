#!/usr/bin/env python

# NOTE: Twitter ATOM feed expected to stop working soon
# Will have to transition to OAuth framework

import urllib
import json

def readConfig(filename):
    f = open('./config/'+filename,'r')
    FILE = f.read()
    f.close()

    JSON = json.loads(FILE)
    return JSON

Config = readConfig('config.json')

# Will modify config coding to handle list of dicts
# Can set to iterate through various sources, or pick at random?

endpoint = Config['url']
name = Config['name']

response = urllib.urlopen(endpoint)

JSON = response.read()

FEED = json.loads(JSON)

for entry in FEED:
    text = entry['text']
    created_at = entry['created_at']
    user_image = entry['user']['profile_background_image_url']

    print name
    print text
    print created_at
    print user_image
    print "==============="


