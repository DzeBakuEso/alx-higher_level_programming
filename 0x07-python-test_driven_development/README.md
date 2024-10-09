# 0x07. Python - Test-Driven Development

## Background Context
Starting from today, it is essential to prioritize writing documentation (module(s) + function(s)) and tests before coding any functionality. This approach supports Test-Driven Development (TDD), helping to identify edge cases and ensuring comprehensive test coverage.

## Important Notice
- The intranet checks for Python projects will not be released before their first deadline to allow you to focus on TDD.
- Collaborating on test cases is encouraged to avoid missing edge cases, but implementation should be individual.
- Always assume potential edge cases when testing user inputs.

## Learning Objectives
By the end of this project, you should be able to explain:

- Why Python programming is awesome.
- What constitutes an interactive test.
- The importance of tests.
- How to write docstrings for creating tests.
- How to document each module and function effectively.
- Basic option flags to create tests.
- Strategies for identifying edge cases.

## Resources
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://realpython.com/python-testing/#unit-testing)

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs.
- All files must be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- All files should end with a newline.
- The first line of all files must be: `#!/usr/bin/python3`.
- A `README.md` file, located at the root of the project folder, is mandatory.
- Code must comply with `pycodestyle` (version 2.8.*).
- All files must be executable.
- The length of files will be assessed using `wc`.

### Python Test Cases
- Allowed editors: vi, vim, emacs.
- All files must end with a newline.
- All test files should be in a folder named `tests`.
- All test files should be text files with the extension `.txt`.
- All tests must be executed using the command: `python3 -m doctest ./tests/*`.
- Each module must have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- Each function must have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- Documentation must provide a clear and concise explanation of the module, class, or method.
  
## Copyright - Plagiarism
- Solutions must be original and not copied from others.
- Publishing any content from this project is strictly prohibited.
- Any form of plagiarism will result in removal from the program.

## Tasks Overview
1. **Integers Addition**: Write a function that adds two integers.
2. **Divide a Matrix**: Create a function to divide all elements of a matrix.
3. **Say My Name**: Develop a function that prints "My name is <first name> <last name>".
4. **Print Square**: Implement a function that prints a square using the character `#`.
5. **Text Indentation**: Write a function that prints text with two new lines after specified punctuation marks.
6. **Max Integer - Unittest**: Create unittests for a function that finds the maximum integer in a list.

## Repo Details
- **GitHub Repository**: [alx-higher_level_programming](https://github.com/yourusername/alx-higher_level_programming)
- **Directory**: `0x07-python-test_driven_development`
- **Files**:
  - `0-add_integer.py`, `tests/0-add_integer.txt`
  - `2-matrix_divided.py`, `tests/2-matrix_divided.txt`
  - `3-say_my_name.py`, `tests/3-say_my_name.txt`
  - `4-print_square.py`, `tests/4-print_square.txt`
  - `5-text_indentation.py`, `tests/5-text_indentation.txt`
  - `6-max_integer.py`, `tests/6-max_integer_test.py`

