"""
Handles following from pre-requisite.
●	Read inputs from a file located in a separate sub-folder.
●	Write a main function on a different file that calls all functions
"""

import json
class JsonHandler:
    def __init__(self, filepath):
        """Initialization tasks"""
        self.filepath = filepath

    def get_json_content(self):
        """Get Json data from the json file and return it."""
        with open(self.filepath, 'r') as file:

            data = json.load(file)

        return data


