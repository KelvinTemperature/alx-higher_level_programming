#!/usr/bin/python3
""" Script to display the value of X-Request-Id variable """
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
