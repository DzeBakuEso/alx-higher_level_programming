#!/usr/bin/python3
"""Fetches a URL and displays the value of the 'X-Request-Id' header."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Extract and print the value of 'X-Request-Id' from the response header
    print(response.headers.get('X-Request-Id'))
