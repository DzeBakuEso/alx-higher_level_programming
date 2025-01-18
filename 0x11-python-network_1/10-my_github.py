#!/usr/bin/python3
"""Fetches GitHub user id using Basic Authentication with a personal access token."""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get the GitHub username and personal access token from arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL to fetch user details
    url = "https://api.github.com/user"
    
    # Make the GET request with Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    # Check if the request was successful
    if response.status_code == 200:
        # If successful, print the user ID
        print(response.json().get('id'))
    else:
        # If unsuccessful, print None (GitHub API responds with 404, 403, etc.)
        print("None")
