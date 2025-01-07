#!/usr/bin/python3
"""
Fetches and lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assuming State model is in model_state.py

# Add the parent directory to the Python path so that 'models' is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.city import city  # Now correctly pointing to models.city

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) < 4:
        print("Usage: ./<script_name> <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Create an engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the cities along with their associated state names
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
