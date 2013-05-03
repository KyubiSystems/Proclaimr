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

FEED0= FEED[0]

print name
print '==========='

for key, value in FEED0.iteritems():
    print key+":", value

