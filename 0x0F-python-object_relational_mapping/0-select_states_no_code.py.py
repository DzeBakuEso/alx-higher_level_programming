#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import State, Base
import sys

if __name__ == "__main__":
    # Get arguments passed to the script: MySQL username, password, & database name
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Create the engine to connect to MySQL using the MySQLdb driver
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(username, passwd, db_name), 
            pool_pre_ping=True
        )

        # Create tables in the database based on models (if not already created)
        Base.metadata.create_all(engine)

        # Open a session to interact with the database
        session = Session(engine)

        # Query all states, order by id in ascending order, and print them
        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
