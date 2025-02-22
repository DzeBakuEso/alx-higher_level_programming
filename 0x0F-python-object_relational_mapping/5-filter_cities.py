#!/usr/bin/python3
"""
Lists all cities of a specified state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL credentials and state name from command-line arguments
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

    # Create a cursor to execute the query
    cursor = db.cursor()

    # SQL query to fetch cities in the given state (SQL injection safe)
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch results and format them
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and connection
    cursor.close()
    db.close()

