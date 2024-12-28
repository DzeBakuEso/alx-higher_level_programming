#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """ Get argetns passd to script: MySQL usname, passwd, & datbse name """
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    """ Cnnct to MySQL servr runnng on loclhst at port 3306 wth utf8 chset """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db="hbtn_0e_0_usa",
        charset="utf8"
    )

    """ Create a cursor object to interact with the database """
    cursor = db.cursor()

    """ Execute the query to get all states sorted by id in ascending order """
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    """ Fetch all the results of the query """
    states = cursor.fetchall()

    """ Display the results, printing each state as a tuple (id, name) """
    for state in states:
        print(state)

    """ Close the cursor and database connection after use """
    cursor.close()
    db.close()
