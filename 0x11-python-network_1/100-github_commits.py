#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Get repository and owner from the command-line arguments
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    # GitHub API URL to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    # Set up parameters to limit the number of commits and filter by author
    params = {'author': 'rails', 'per_page': 10}
    
    # Make the GET request to the GitHub API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        commits = response.json()
        
        # Print the 10 most recent commits with the required format
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("None")
