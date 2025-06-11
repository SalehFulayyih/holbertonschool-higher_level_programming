#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The filename where the JSON should be saved.

    If the file exists, it will be overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Parameters:
        filename (str): The JSON file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
