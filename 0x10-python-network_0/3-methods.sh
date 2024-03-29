#!/bin/bash
#Displays all HTTP methods the servver will accept
curl -sI -X OPTIONS "$1" | grep -i "^ALLOW:" | cut -d " " -f 2-
