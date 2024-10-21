# 0x0C. Python - Almost a Circle

## Description
This project is part of the ALX Higher Level Programming curriculum and focuses on object-oriented programming (OOP) in Python. It includes creating classes and managing their attributes, serialization, deserialization, and unit testing.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Resources
Read or watch:
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://docs.python.org/3/library/unittest.html#unittest.TestCase)

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: 
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified).

### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest` module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: e.g., for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases so that you don’t miss any edge case.

## Tasks
### 0. If it's not tested it doesn't work
- All your files, classes, and methods must be unit tested and be PEP 8 validated.

### 1. Base class
- Write the first class `Base` in `models/base.py`:
  - Private class attribute `__nb_objects = 0`
  - Class constructor: `def __init__(self, id=None)`

### 2. First Rectangle
- Write the class `Rectangle` that inherits from `Base` in `models/rectangle.py`:
  - Private instance attributes with public getter and setter.
  - Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`

### 3. Validate attributes
- Update the class `Rectangle` by adding validation of all setter methods and instantiation (id excluded).

### 4. Area first
- Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the Rectangle instance.

### 5. Display #0
- Update the class `Rectangle` by adding the public method `def display(self):` that prints the Rectangle instance with the character `#`.

### 6. __str__
- Update the class `Rectangle` by overriding the `__str__` method.

### 7. Display #1
- Improve the public method `def display(self):` to consider `x` and `y`.

### 8. Update #0
- Add the public method `def update(self, *args):` that assigns an argument to each attribute.

### 9. Update #1
- Update the public method `def update(self, *args, **kwargs)` to handle key-value arguments.

### 10. And now, the Square!
- Write the class `Square` that inherits from `Rectangle` in `models/square.py`.

## Repository
- GitHub repository: [alx-higher_level_programming](https://github.com/YOUR_USERNAME/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`

