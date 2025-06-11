#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML format and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML data to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserializes XML content from a file and returns a dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: A dictionary reconstructed from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except (ET.ParseError, FileNotFoundError):
        return None
