# 0x0F. Python - Object-relational Mapping

## Project Overview
In this project, you will link two powerful worlds: Databases and Python! You will first use the `MySQLdb` module to connect to a MySQL database and execute SQL queries. Then, you will transition to using SQLAlchemy, an Object-Relational Mapper (ORM), which allows you to interact with your database without writing SQL queries directly. This project provides an opportunity to understand the difference between writing raw SQL and using ORM for database manipulation.

**Project Weight:** 1  
**Start Date:** Dec 18, 2024, 6:00 PM  
**Deadline:** Jan 1, 2025, 6:00 PM  
**Checker Released:** Dec 22, 2024, 6:00 AM  
**Auto Review Launch:** At the Deadline

## Before You Start
Please ensure that your MySQL server is running version 8.0. You can follow this guide to install MySQL 8.0 on Ubuntu 20.04.

### Background Context
In the first part of this project, you will be using the `MySQLdb` module to interact with a MySQL database. In the second part, you will use SQLAlchemy, an ORM tool that abstracts database operations into Python code. With ORM, you no longer need to write SQL queries directly; instead, you'll interact with your database using Python objects.

### Example Comparison
Without ORM:
```python
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import State, Base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()

Resources
Object-relational mappers
MySQLdb documentation
SQLAlchemy documentation
Introduction to SQLAlchemy
SQLAlchemy ORM Tutorial for Python Developers
Learning Objectives
At the end of this project, you will be able to:

Explain why Python programming is awesome.
Connect to a MySQL database from a Python script.
SELECT and INSERT rows in a MySQL table using Python.
Understand ORM concepts and map Python classes to MySQL tables.
Create and use Python Virtual Environments.
Requirements
General
Allowed Editors: vi, vim, emacs.
Files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
Use MySQLdb version 2.0.x and SQLAlchemy version 1.4.x.
All files should end with a new line.
The first line of all files should be exactly #!/usr/bin/python3.
A README.md file is required.
Your code should be formatted using pycodestyle (version 2.8.x).
All files must be executable.
All modules, classes, and functions must have documentation.
Installation
1. Setting up a Python Virtual Environment
To install the required dependencies for the project:

$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient

$ sudo pip3 install SQLAlchemy

Author Dzeble Kwame 
