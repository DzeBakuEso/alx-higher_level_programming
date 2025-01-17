#!/bin/bash
# Send a JSON POST request to the URL with the contents of a JSON file passed as the second argument

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
