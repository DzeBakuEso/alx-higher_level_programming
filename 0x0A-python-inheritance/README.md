# 0x0A. Python - Inheritance

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when, and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (e.g., `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be a complete sentence explaining the purpose of the module, class, or method (the length will be verified)
- We strongly encourage you to work together on test cases to ensure you don’t miss any edge cases

### Documentation
- Do not use the words `import` or `from` inside your comments, as the checker will think you are trying to import some modules.

## Quiz Questions
Great! You've completed the quiz successfully! Keep going!

## Tasks

### 0. Lookup
- **Mandatory**
- Write a function that returns the list of available attributes and methods of an object.
- **Prototype**: `def lookup(obj):`
- Returns a list object
- You are not allowed to import any module

### 1. My list
- **Mandatory**
- Write a class `MyList` that inherits from `list`:
  - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
  - You can assume that all the elements of the list will be of type `int`
  - You are not allowed to import any module

### 2. Exact same object
- **Mandatory**
- Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise, `False`.
- **Prototype**: `def is_same_class(obj, a_class):`
- You are not allowed to import any module

### 3. Same class or inherit from
- **Mandatory**
- Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from the specified class; otherwise, `False`.
- **Prototype**: `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

### 4. Only sub class of
- **Mandatory**
- Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, `False`.
- **Prototype**: `def inherits_from(obj, a_class):`
- You are not allowed to import any module

### 5. Geometry module
- **Mandatory**
- Write an empty class `BaseGeometry`.
- You are not allowed to import any module

### 6. Improve Geometry
- **Mandatory**
- Write a class `BaseGeometry` (based on `5-base_geometry.py`).
  - Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
- You are not allowed to import any module


