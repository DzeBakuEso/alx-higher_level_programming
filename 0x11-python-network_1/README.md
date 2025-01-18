## 0x11. Python - Network #1

### Description
This project focuses on utilizing Python to interact with web resources and APIs. Key objectives include making HTTP requests, handling responses, and manipulating external data using libraries such as `urllib` and `requests`. Additionally, this project builds on skills related to error handling and working with JSON data.

### Learning Objectives
At the end of this project, you will be able to:
- Fetch internet resources using the Python `urllib` package.
- Decode `urllib` body responses.
- Use the `requests` package to simplify HTTP requests.
- Make HTTP GET, POST, and other requests.
- Fetch and process JSON resources.
- Manipulate and extract data from external services.

### Requirements
#### General
- **Editors:** `vi`, `vim`, `emacs`
- **Environment:** All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- **Code Style:** Files must follow `pycodestyle` (version 2.8.*).
- **Execution:** All files must be executable and start with `#!/usr/bin/python3`.
- **Documentation:**
  - Modules, classes, and methods must include descriptive docstrings.
  - Code should not execute when imported (use `if __name__ == "__main__":`).
- **File Structure:** All files must end with a new line and their lengths will be checked using `wc`.

### Resources
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://docs.python-requests.org/en/master/user/quickstart/)
- [Requests package documentation](https://docs.python-requests.org/en/master/)

### Tasks
#### 0. What's my status? #0
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib`.
- Requirements:
  - The response body must be displayed in a specific format.
  - Use a `with` statement for file handling.

#### 1. Response header value #0
Write a Python script that fetches a URL and displays the `X-Request-Id` header value using `urllib` and `sys`.
- The header value will vary with each request.

#### 2. POST an email #0
Write a Python script that sends a POST request to a URL with an email as a parameter, displaying the response body in UTF-8.
- Use `urllib` and `sys`.

#### 3. Error code #0
Write a Python script that fetches a URL and handles HTTP errors gracefully.
- Print `Error code: <HTTP status>` for errors.
- Use `urllib.error.HTTPError` for error handling.

#### 4. What's my status? #1
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `requests`.
- Simplify the response handling compared to `urllib`.

#### 5. Response header value #1
Write a Python script to fetch a URL and display the `X-Request-Id` header value using `requests`.

#### 6. POST an email #1
Write a Python script that sends a POST request to a URL with an email address as a parameter using `requests`.

#### 7. Error code #1
Write a Python script to fetch a URL and display the response body or error code for HTTP errors using `requests`.

#### 8. Search API
Write a Python script that sends a POST request with a letter to `http://0.0.0.0:5000/search_user` and processes the JSON response.
- Display the ID and name if valid.
- Handle invalid or empty JSON responses.

#### 9. My GitHub!
Write a Python script that uses Basic Authentication to display your GitHub ID using the GitHub API.
- Use `requests`.

### Repository Structure
- **GitHub Repository:** `alx-higher_level_programming`
- **Directory:** `0x11-python-network_1`

### How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-higher_level_programming/0x11-python-network_1
   ```
3. Run the scripts with the required arguments.

### Author
- Dzeble kwame

