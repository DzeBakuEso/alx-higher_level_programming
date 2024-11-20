# 0x0D. SQL - Introduction

## Description
This project introduces the fundamentals of **SQL** and **MySQL**, focusing on basic database concepts, SQL syntax, and MySQL functionalities. By the end of this project, you will have a foundational understanding of relational databases and how to interact with them using SQL queries. 

This project is part of the **[curriculum]** and aims to develop your understanding of databases, including creating, modifying, and querying databases and tables.

---

## Learning Objectives
At the end of this project, you should be able to explain the following concepts without external help:

### General
- **What is a database?**
- **What is a relational database?**
- **What does SQL stand for?**
- **What is MySQL?**
- How to:
  - Create a database in MySQL.
  - Differentiate between DDL and DML.
  - Use SQL statements to:
    - **CREATE** or **ALTER** a table.
    - **SELECT** data from a table.
    - **INSERT**, **UPDATE**, or **DELETE** data.
  - Write and execute subqueries.
  - Use MySQL functions effectively.

---

## Resources
To complete this project, refer to the following resources:

- [What is Database & SQL?](https://)
- [A Basic MySQL Tutorial](https://)
- [Basic SQL statements: DDL and DML](https://)
- [Basic queries: SQL and RA](https://)
- [SQL technique: functions](https://)
- [SQL technique: subqueries](https://)
- [What makes the big difference between a backtick and an apostrophe?](https://)
- [MySQL Cheat Sheet](https://)
- [MySQL 8.0 SQL Statement Syntax](https://)
- [Installing MySQL in Ubuntu 20.04](https://)

---

## Project Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- Files will be executed on **Ubuntu 20.04 LTS** with **MySQL 8.0 (version 8.0.25)**.
- All files must end with a new line.
- Include comments in SQL queries to describe their purpose.
- SQL keywords (e.g., `SELECT`, `WHERE`) must be written in uppercase.
- A `README.md` file at the root of the project folder is mandatory.
- File length will be tested using `wc`.

### Comments in SQL Files
Example:
```sql
-- Select the 3 most recently created students from Batch ID = 3
SELECT id, name 
FROM students 
WHERE batch_id = 3 
ORDER BY created_at DESC 
LIMIT 3;

