from input_handler import JsonHandler
from question_set_2.program_1 import WordFrequency
if __name__=="__main__":
    print("Welcome to Main program")

    print("++++++ Program - 1 +++++++++++")
    print("Read from json(present in subdir) and prints its contents")
    json_handler_obj = JsonHandler("inputs/input1.json")
    json_data = json_handler_obj.get_json_content()
    print(json_data)

    print("++++++++ Program - 2 ++++++++++++++")
    print("Get the frequency of words in a string")
    word_freq_obj = WordFrequency("which is better python 2 or python 3")
    word_freq_obj.get_word_frequency()