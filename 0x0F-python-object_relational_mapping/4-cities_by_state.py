#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, showing city id, city name,
and state name in ascending order by city id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # SQL query to fetch city details with corresponding state names
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch and display results
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    db.close()
