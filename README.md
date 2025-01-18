# AirBnB Clone - The Console

## Description
This repository contains the first phase of the AirBnB clone project: the Console. This project is part of the ALX Software Engineering program. The goal is to build a clone of the AirBnB platform, beginning with the backend components and gradually progressing to the frontend.

The Console is a command-line interface (CLI) tool for managing various objects in the AirBnB clone system, including users, places, states, cities, and amenities. It enables the creation, retrieval, updating, and deletion of objects while ensuring persistent storage.

---

## Features
- Interactive and non-interactive modes.
- Object management (CRUD operations).
- Data serialization and deserialization to/from JSON format.
- Extensible command interpreter.

---

## Files and Structure
- **`console.py`**: The main console program.
- **`models/`**: Contains the classes for all data models and the storage engine.
  - `base_model.py`: The base class for all models.
  - `user.py`: A subclass for managing user objects.
  - `state.py`, `city.py`, `place.py`, `amenity.py`, `review.py`: Other subclasses representing various objects.
- **`README.md`**: This documentation file.
- **`tests/`**: Contains all unit tests for the application.

---

## Requirements
- Python 3.8 or higher.
- All scripts begin with the line `#!/usr/bin/python3`.
- Compatible with Ubuntu 20.04 LTS.
- Code adheres to `pycodestyle` (PEP 8).

---

## How to Use the Console
### Interactive Mode:
Run the console interactively:
```bash
./console.py

Author: Dzeble Kwame
