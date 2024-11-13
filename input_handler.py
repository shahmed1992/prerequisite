"""
Handles following from pre-requisite.
●	Read inputs from a file located in a separate sub-folder.

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

if __name__=="__main__":
    print("Welcome to input handler program")
    json_handler_obj = JsonHandler("inputs/input1.json")
    json_data = json_handler_obj.get_json_content()
    print(json_data)
