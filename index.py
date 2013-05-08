#!/usr/bin/env python

# NOTE: Twitter ATOM feed expected to stop working soon
# Will have to transition to OAuth framework

import urllib
import json
import cgi
import cgitb

from datetime import datetime
from pretty_date import pretty_date
from file_utils import readConfig

# Enable CGI traceback

cgitb.enable()

# Read config file

Config = readConfig('config.json')

# Will modify config coding to handle list of dicts
# Can set to iterate through various sources, or pick at random?

endpoint = Config['url']
name = Config['name']

# Print Content-Type: header + blank line
print "Content-Type: text/html"
print 

# Read response, and parse to Python data structure via JSON
# Need some exception handling here for endpoint unavailable

response = urllib.urlopen(endpoint)
JSON = response.read()
FEED = json.loads(JSON)

# Get CGI parameter 'page=?' pointing to page number

form = cgi.FieldStorage()
if "page" not in form:
    page = 0
else:
    page = int(form["page"].value)

# Select page # from feed

entry = FEED[page]

# extract parameters
# Wed May 08 12:34:39 +0000 2013

text = entry['text']
created_at = datetime.strptime(entry['created_at'],"%a %b %d %H:%M:%S +0000 %Y")

time_since = pretty_date(created_at)

user_image = entry['user']['profile_background_image_url']

# print output HTML, should be a template

print '<html><head><title>'+name+'</title></head>'
print '<img src="'+user_image+'">'
print '<body><h1>'+text+' </h1>'
print '<h3>'+name+': '+time_since+'</h3>'
print '</body></html>'


