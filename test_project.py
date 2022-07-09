'''
The testing was so challenging for me that i regreted that I chose this program to do for the final praject. 
It is because, the function i wrote requires multiple input and for some function, it is the side effect that i assert. 
So this is to inform CS50 that i imported someones library that mocks keyboard input and collect side effects. 
The module called tud_test_base.py is forked from https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
'''


import pytest
from project import validate, encrypt_file, decrypt_file, Exit_program, User_Function
from tud_test_base import get_display_output, set_keyboard_input


User_Names = [{"User_Name": "UserTest1", "PassWord": "12345"}]
User_NamesL = ["UserTest1"]


Un_data = "This is a test file to encrypt"


with open("test_file.txt", "w") as file:
    file.write(Un_data)
    


#The test begins

def test_validate1():
    with pytest.raises(SystemExit):
        set_keyboard_input(["12345", "12345", "12345"])

        validate("UserTest1") == True

    #output = get_display_output("Password: ")
    

def test_validate2():
    set_keyboard_input(["1", "0000", "0000"])

    assert validate("UserTest2") == True

    #output = get_display_output("User Name not found!!!", "Create New user? (Y/N) ", "Input password: ", "Confirm password: ")


def test_validate3():

    set_keyboard_input(["1", "0000", "0100"])

    assert validate("UserTest2") == False

    #output = get_display_output("User Name not found!!!", "Create New user? (Y/N) ", "Input password: ", "Confirm password: ")


def test_encrypt_file():
    encrypt_file("test_file.txt")
    with open("test_file.txt", "r") as file:
            test_data = file.read()

    assert Un_data != test_data


def test_decrypt_file():
    decrypt_file("test_file.txt")
    with open("test_file.txt", "rb") as file:
        test_data = file.read()

    assert b'This is a test file to encrypt' == test_data


def test_Exit_program():
    with pytest.raises(SystemExit):
        assert Exit_program()


def test_User_Function():
    ...
    pass
