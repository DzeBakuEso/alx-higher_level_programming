#!/usr/bin/python3
"""This module defines the Student class with JSON serialization and deserialization."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in that list
        are retrieved.

        Args:
            attrs (list): Optional list of attributes to filter.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary representing the new attribute values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
