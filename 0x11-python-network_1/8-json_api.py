#!/usr/bin/python3
""" Script that POST a letter and JSONfy the response """
import requests
import sys


if __name__ == '__main__':
    data = {'q': ""}
    try:
        data['q'] = sys.argv[1]
    except Exception:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_file = r.json()

        if not json_file:
            print('No result')
        else:
            print('[{}] {}'.format(json_file.get('id'), json_file.get('name')))
    except Exception:
        print('No a valid JSON')
