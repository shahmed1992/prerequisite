from input_handler import JsonHandler

if __name__=="__main__":
    print("Welcome to input handler program")
    json_handler_obj = JsonHandler("inputs/input1.json")
    json_data = json_handler_obj.get_json_content()
    print(json_data)