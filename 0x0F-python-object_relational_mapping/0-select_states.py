#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments passed to the script: MySQL username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get all states sorted by id in ascending order
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    states = cursor.fetchall()

    # Display the results, printing each state as a tuple (id, name)
    for state in states:
        print(state)

    # Close the cursor and database connection after use
    cursor.close()
    db.close()
