"""
write a function for the below scenario.
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
○	At least 1 letter between [a-z]
○	At least 1 number between [0-9]
○	At least 1 letter between [A-Z]
○	At least 1 character from [$#@]
○	Minimum length of transaction password: 6
○	Maximum length of transaction password: 12

Your function should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma
Example -
input_password =asqwr1234@1,aF145#,2w3E*,2We3345 Output = asqwr1234@1

"""

class PasswordChecker:
    def __init__(self):
        self.list_of_pwds = ["asqwr1234@1","aF145#","2w3E*","2We3345"]

    def check_password(self):
        for pwd in self.list_of_pwds:
            print(f"Validation of Password: {pwd}")
