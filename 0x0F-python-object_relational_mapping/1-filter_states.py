#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """
    List all states with a name starting with 'N' from the database.
    Arguments: mysql username, mysql password, database name.
    """

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

    # Execute the query to find states starting with 'N'
    query = "SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and print the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
