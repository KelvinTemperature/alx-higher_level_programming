#!/bin/bash
#script make request to URL and cause the server to respond with a string
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!"
