# Python Classes and Objects - Square

## Description

This repository contains implementations of different functionalities for creating and manipulating squares using Python classes. The project focuses on learning Object-Oriented Programming (OOP) in Python, particularly around classes, attributes, methods, and encapsulation. Each class defines a square with various functionalities, such as validation, area calculation, and printing.

## Requirements

### General
- **Allowed editors**: vi, vim, emacs
- **Python version**: All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3 (version 3.8.5)`
- **File format**: All files should end with a new line
- **Shebang**: The first line of all files should be `#!/usr/bin/python3`
- **README.md**: A `README.md` file is mandatory at the root of the project folder
- **Code style**: Code should adhere to `pycodestyle (version 2.8.*)`
- **Executable files**: All files must be executable
- **File length check**: The length of the files will be tested using `wc`

### Documentation Requirements
- Each **module** should have documentation: `python3 -c 'print(__import__("module_name").__doc__)'`
- Each **class** should have documentation: `python3 -c 'print(__import__("module_name").ClassName.__doc__)'`
- Each **function** (inside and outside classes) should have documentation: 
    - `python3 -c 'print(__import__("module_name").function_name.__doc__)'`
    - `python3 -c 'print(__import__("module_name").ClassName.function_name.__doc__)'`
- Documentation should provide real sentences explaining the purpose of the module, class, or method.

## Tasks

### 0. My First Square
- **File**: `0-square.py`
- **Description**: Write an empty class `Square` that defines a square.
- **Example**:
    ```bash
    ./0-main.py
    <class '0-square.Square'>
    {}
    ```

### 1. Square with Size
- **File**: `1-square.py`
- **Description**: Write a class `Square` that defines a square with a private instance attribute `size` and instantiation method.
- **Example**:
    ```bash
    ./1-main.py
    'Square' object has no attribute '__size'
    ```

### 2. Size Validation
- **File**: `2-square.py`
- **Description**: Extend the `Square` class by adding validation for the size attribute.
    - Raise `TypeError` if size is not an integer
    - Raise `ValueError` if size is less than 0
- **Example**:
    ```bash
    ./2-main.py
    size must be an integer
    size must be >= 0
    ```

### 3. Area of a Square
- **File**: `3-square.py`
- **Description**: Add a public instance method `area(self)` that returns the area of the square.
- **Example**:
    ```bash
    ./3-main.py
    Area: 9
    ```

### 4. Access and Update Private Attribute
- **File**: `4-square.py`
- **Description**: Add getter and setter methods for the size attribute.
    - Getter: `def size(self)`
    - Setter: `def size(self, value)`
    - Validate the size in the setter method.
- **Example**:
    ```bash
    ./4-main.py
    size must be an integer
    ```

### 5. Printing a Square
- **File**: `5-square.py`
- **Description**: Add a public instance method `my_print(self)` that prints the square using the `#` character.
    - Print an empty line if the size is 0.
- **Example**:
    ```bash
    ./5-main.py
    ###
    ###
    ###
    ```

### 6. Coordinates of a Square
- **File**: `6-square.py`
- **Description**: Add a `position` private instance attribute with getter and setter methods.
    - `position` must be a tuple of 2 positive integers.
    - Modify `my_print(self)` to account for the position.
- **Example**:
    ```bash
    ./6-main.py | tr " " "_" | cat -e
    ###$
    ###$
    ###$
    ```

## Repository

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x06-python-classes`

## More Information

This project emphasizes the importance of **encapsulation** and **data hiding** in Python. It introduces methods such as getters and setters to protect and validate private attributes. Moreover, the usage of docstrings is heavily encouraged to ensure code clarity and maintainability.


