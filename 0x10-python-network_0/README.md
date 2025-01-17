# 0x10. Python - Network #0

## Description

This project focuses on understanding HTTP requests, responses, headers, and how to make requests using `curl` in the context of a backend API. It also includes writing Bash scripts to interact with HTTP services.

## Learning Objectives

At the end of this project, you should be able to explain the following concepts:

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- A `README.md` file is mandatory at the root of the folder of the project
- All scripts will be tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long (`wc -l file` should print 3)
- All files should end with a new line
- All files must be executable
- The first line of all your Bash files should be exactly `#!/bin/bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All `curl` commands must have the option `-s` (silent mode)
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- Your code should use `pycodestyle` (version 2.8.*)
- All your modules should be documented using Python’s documentation standards
- All your classes should be documented
- All your functions (inside and outside a class) should be documented

## Tasks

### 0. cURL Body Size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

- The size must be displayed in bytes.
- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `0-body_size.sh`

### 1. cURL to the End

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

- Display only the body of a 200 status code response.
- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `1-body.sh`

### 2. cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `2-delete.sh`

### 3. cURL Only Methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `3-methods.sh`

### 4. cURL Headers

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.

- A header variable `X-School-User-Id` must be sent with the value `98`.
- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `4-header.sh`

### 5. cURL POST Parameters

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

- A variable `email` must be sent with the value `test@gmail.com`.
- A variable `subject` must be sent with the value `I will always be here for PLD`.
- You have to use `curl`.
- Test your script using the sandbox provided.

**File:** `5-post_params.sh`

### 6. Find a Peak

Write a function that finds a peak in a list of unsorted integers.

- The function should be named `find_peak`.
- You are not allowed to import any module.
- Your algorithm must have the lowest complexity.
- You must provide the function and its complexity in separate files.

**File:** `6-peak.py`
**Complexity File:** `6-peak.txt`

## Resources

- Read or watch the following resources:
  - HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation, “Options MultiView” and Character Set Negotiation)
  - HTTP Cookies

## GitHub Repository

- Repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)
- Directory: `0x10-python-network_0`
AUTHOR: Dzeble kwame
