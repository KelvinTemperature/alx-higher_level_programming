#!/bin/bash
#Script to get the size of the body of a URL
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
