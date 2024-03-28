#!/bin/bash
#script to display only the response code
curl -so /dev/null -w "%{http_code}" "$1"
