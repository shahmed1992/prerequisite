from input_handler import JsonHandler
from question_set_2.program_1 import WordFrequency
from question_set_2.program_2 import CircularQueueUsingDict
from question_set_2.program_3 import PasswordChecker
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

    print("++++++++ Program - 3 ++++++++++++++")
    print("Circular Queue Using dictionary")
    cir_queue_obj = CircularQueueUsingDict()
    cir_queue_obj.demo_cir_queue_working()

    print("++++++++ Program - 4 ++++++++++++++")
    print("Password Validator from User ")
    pwd_checker_obj = PasswordChecker()
    pwd_checker_obj.check_password()