#!/usr/bin/python3
"""
Defines the State class and Base instance for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance
Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id, a primary key that is auto-generated.
        name (str): The state's name, a string of up to 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
