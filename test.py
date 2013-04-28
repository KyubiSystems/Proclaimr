#!/usr/bin/env python

import urllib
import json

# This is expected to stop working soon :-(
# Will have to transition to OAuth

endpoint = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=BIS_spaceflight"

response = urllib.urlopen(endpoint)

JSON = response.read()

FEED = json.loads(JSON)

print FEED[0]['text']
print FEED[0]['created_at']



