from cryptography.fernet import Fernet
import pytest
from Final import validate, encrypt_file, decrypt_file, Exit_program
from Final import User_Function
#from Final.User_Function.User import get_numb, create_new_contact, update_e_contact, list_all_contacts, by_name, by_numb, one_file, all_file, export_to_pdf



User_Names = [{"User_Name": "UserTest1", "PassWord": "12345"}]
User_NamesL = ["UserTest1"]
userAfileD = {"A": "1", "B": "2"}
userAfile = ["A", "B"]



affirmation_L = ["1", "y", "yes", "k", "ok", "okay", "okey"]

Un_data = "This is a test file to encrypt"
key = Fernet.generate_key()
with open("test_file.txt", "w") as file:
    file.write(Un_data)
    


#def test_validate():


def test_encrypt_file():
    encrypt_file("test_file.txt")
    with open("test_file.txt", "r") as file:
            test_data = file.read()
    f = Fernet(key)
    En_data = f.encrypt('This is a test file to encrypt')

    assert En_data == test_data


def test_decrypt_file():
    decrypt_file("test_file.txt")
    with open("test_file.txt", "rb") as file:
        test_data = file.read()

    assert b'This is a test file to encrypt' == test_data

def test_Exit_program():
    with pytest.raises(SystemExit):
        assert Exit_program()

#def test_
