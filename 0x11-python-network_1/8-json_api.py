#!/usr/bin/python3
"""Sends a POST request to a URL with a letter and handles the JSON response."""

import requests
import sys

if __name__ == "__main__":
    # Get the letter argument or set it to an empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Define the URL for the POST request
    url = "http://0.0.0.0:5000/search_user"
    
    # Send the POST request with the letter as parameter q
    response = requests.post(url, data={'q': letter})
    
    try:
        # Attempt to parse the response as JSON
        json_response = response.json()
        
        # Check if the response is empty
        if not json_response:
            print("No result")
        else:
            # Print the id and name from the JSON response
            print(f"[{json_response['id']}] {json_response['name']}")
    
    except ValueError:
        # If JSON parsing fails, print an error message
        print("Not a valid JSON")
