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

    print '<html><head><title>'+name+'</title></head>'
    print '<img src="'+user_image+'">'
    print '<body><h1>'+text+' </h1>'
    print '<h3>'+created_at+'</h3>'
    print '</body></html>'
    print "==============="


