#!/usr/bin/python3
# Script to display body of URl and handle Error
from urllib import request, error
import sys


try:
    with request.urlopen(sys.argv[1]) as response:
        body = response.read()
        print(body.decode('utf-8'))
except error.HTTPError as e:
    print('Error code: {}'.format(e.code))
