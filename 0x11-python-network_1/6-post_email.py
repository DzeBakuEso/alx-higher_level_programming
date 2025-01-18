#!/usr/bin/python3
"""Sends a POST request with an email address and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)

    # Display the body of the response
    print("Your email is: {}".format(response.text))
