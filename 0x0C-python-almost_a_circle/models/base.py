# models/base.py
class Base:
    """Base class for managing the id attribute across all objects"""

    __nb_objects = 0  # private class attribute to track the number of objects

    def __init__(self, id=None):
        """Initialize the base class

        Args:
            id (int): The id for the instance (optional).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
