#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me that triggers the response "You got me!"

curl -s -X PUT -H "Origin: You got me!" 0.0.0.0:5000/catch_me
