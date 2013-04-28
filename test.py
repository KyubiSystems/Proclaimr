#!/usr/bin/env python

import urllib
import json

# This is expected to stop working soon :-(
# Will have to transition to OAuth

endpoint = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=BIS_spaceflight"

response = urllib.urlopen(endpoint)

JSON = response.read()

FEED = json.loads(JSON)

FEED0= FEED[0]

for key, value in FEED0.iteritems():
    print key+":", value



