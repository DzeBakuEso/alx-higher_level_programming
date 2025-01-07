#!/usr/bin/python3
"""
Contains the class definition of a State and the Base class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # Import relationship here

Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Lazy import of City to avoid circular import
    @property
    def cities(self):
        from model_city import City  # Import City here to avoid circular import
        return self._cities

    # Setup a relationship between State and City
    _cities = relationship("City", back_populates="state")
