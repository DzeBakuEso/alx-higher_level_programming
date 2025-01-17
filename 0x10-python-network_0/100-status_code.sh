#!/bin/bash
# Send a request to the URL passed as an argument and display the status code

curl -o /dev/null -s -w "%{http_code}" "$1"
