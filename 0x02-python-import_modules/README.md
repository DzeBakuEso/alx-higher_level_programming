# 0x02. Python - import & modules

## Requirements
- All Python files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code should follow the PEP 8 style (pycodestyle 2.8.*)
- Files must be executable and end with a new line
- A `README.md` file is mandatory

## Learning Objectives
By the end of this project, you will be able to:
- Understand the basics of Python modules and how to use them
- Import functions from another file and use them
- Work with command-line arguments
- Use the built-in function `dir()`
- Prevent code execution when a script is imported

## Tasks

### 0. Import a simple function from a simple file
**File**: `0-add.py`

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- Use the `print` function with string formatting to display integers.
- Assign the value `1` to a variable `a` and the value `2` to a variable `b`.
- The program should print: `<a> + <b> = <add(a, b)>` followed by a new line.
- The word `add_0` should only appear once in your code.
- Your program should not be executed when imported.

### 1. My first toolbox!
**File**: `1-calculation.py`

Write a program that imports functions from the file `calculator_1.py`, does some math, and prints the result.

- Define the value `10` to a variable `a` and `5` to a variable `b`.
- Use the functions `add`, `sub`, `mul`, and `div` from `calculator_1.py`.
- Print the result for each operation.
- The word `calculator_1` should only be used once in your file.
- Your program should not be executed when imported.

### 2. How to make a script dynamic!
**File**: `2-args.py`

Write a program that prints the number of and the list of its arguments.

- Output should display the number of arguments and each argument with its position.
- Use the `len(argv)` function to count the number of arguments.
- The program should print `0 arguments.` if no arguments are provided.
- Print the position of each argument starting from 1.

### 3. Infinite addition
**File**: `3-infinite_add.py`

Write a program that prints the result of the addition of all arguments.

- Cast arguments into integers using `int()`.
- Handle big numbers as well.
- If no arguments are provided, the result should be `0`.

### 4. Who are you?
**File**: `4-hidden_discovery.py`

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

- Only print names that do not start with `__`.
- Your code should not be executed when imported.
- Ensure the program runs in Python 3.8.x.

### 5. Everything can be imported
**File**: `5-variable_load.py`

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

- Do not use `*` for importing or `__import__`.
- Your code should not be executed when imported.

## Repository
- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x02-python-import_modules`

