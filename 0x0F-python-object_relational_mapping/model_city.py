#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # Import relationship here

Base = declarative_base()

class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Setup a relationship between City and State
    state = relationship("State", back_populates="cities")
