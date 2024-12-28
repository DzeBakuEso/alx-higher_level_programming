#!/usr/bin/python3
"""
Fetches a State object by name from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    
    # Create all tables in the database (if not already created)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state by name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Check if the state is found and print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
