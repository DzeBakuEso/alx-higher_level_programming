#!/usr/bin/python3
"""
Updates the name of the state where id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa.
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

    # Query the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If the state exists, update its name
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()
