#!/bin/bash
# Sends an OPTIONS request to the URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
