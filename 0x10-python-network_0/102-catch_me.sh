#!/bin/bash
#script make request to URL and cause the server to respond with a string
curl -Ls 0.0.0.0:5000/catch_me -X PUT -H "You got me!"
