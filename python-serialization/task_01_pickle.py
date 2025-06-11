#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object to the specified file using pickle.

        Args:
            filename (str): The path of the file to serialize the object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            # Could log exception if needed
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from the specified file using pickle.

        Args:
            filename (str): The path of the file to deserialize the object from.

        Returns:
            CustomObject | None: An instance of CustomObject if successful, else None.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
