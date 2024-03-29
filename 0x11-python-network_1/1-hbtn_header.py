#!/usr/bin/python3
# Script to display the X-Request-Id of a URL
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
    print(html.get('X-Request-Id'))
