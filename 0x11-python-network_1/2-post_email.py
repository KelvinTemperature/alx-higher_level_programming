#!/usr/bin/python3
""" Script that sends a post request """

from urllib import request, parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(data)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
