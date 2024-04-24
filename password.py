'''3) Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.'''

import re
def check_password_validity(password):
    #check for length
    if len(password)<6 or len(password)>16:
        return False
    # Check for at least one lowercase letter, one uppercase letter, and one digit
    if not re.search("[a-z]",password) or not re.search("[A-Z]",password) or not re.search("[0-9]",password):
        return False
    # Check for at least one special character
    if not re.search("[$#@]",password):
        return False
    return True
password = input("Enter your password: ")
if check_password_validity(password):
    print("Password is valid.")
else:
    print("Password is not valid")
