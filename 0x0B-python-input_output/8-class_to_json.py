#!/usr/bin/python3
"""returns the dictionary description"""


def class_to_json(obj):
    """returns a serielizable dict"""

    # Get the dictionary of object attributes
    obj_dict = vars(obj)
    # Convert non-serializable types to serializable types
    serializable_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
        elif isinstance(value, (tuple, set)):
            # Convert tuple and set to lists, as aren't directly serializable
            serializable_dict[key] = list(value)
        elif isinstance(value, type(None)):
            # Convert None to a string, as it is not directly serializable
            serializable_dict[key] = "None"
        else:
            # For other types, convert to string representation
            serializable_dict[key] = str(value)

    return serializable_dict
