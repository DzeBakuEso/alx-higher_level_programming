#!/usr/bin/python3
"""Takes a URL, sends a request, and displays the X-Request-Id value."""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader("X-Request-Id")
        print(header_value)
