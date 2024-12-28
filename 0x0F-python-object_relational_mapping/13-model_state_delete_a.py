#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states that contain the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to delete the records
    session.commit()

    # Close the session
    session.close()
