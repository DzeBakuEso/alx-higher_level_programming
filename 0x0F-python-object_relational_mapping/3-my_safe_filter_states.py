#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from SQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
