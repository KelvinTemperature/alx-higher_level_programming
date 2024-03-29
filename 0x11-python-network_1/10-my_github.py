#!/usr/bin/python3
""" Script to take GitHub Credentials and uses
GitHUb API to display my Id """
from requests import get, auth
import sys


if __name__ == '__main__':
    url = 'http://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))
