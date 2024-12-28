#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Display all values in the states table where name matches the argument.
    Arguments: mysql username, mysql password, database name, and state name.
    """

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Use `format` to safely include user input in the query
    query = "SELECT id, name FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
