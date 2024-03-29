#!/usr/bin/python3
""" Script that fetches URL using requests package """
import requests


if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    body = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(body), body))
