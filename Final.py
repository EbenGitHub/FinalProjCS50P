"""
This program creates User account and let them store there contacts
Read README.md file on how to use the program
Create by ABENEZER ESHETIE aka Ebenezer Eshexe
I tried to include all the things i have learnt.

If you have comments or if you want to contact me:
**GitHub User name: Eenrics
**Email Address: ebenezeresh525@gmail.com
**Phone Number: +251955455616

"""
"""

To do before submitting :::
-- Make sure you included all things you have learnt so far. apply it here
-- Write README.md required.txt as needed
-- make test.py to test your functions. Make sure Every Function works fluently
-- add line comment which tells the steps
-- add multi-line comment that tells what the program does
-- Never forget to 'black [file]' your file
-- 
-- Clean up unessasery comments
-- Create edx acc
-- ...


"""


# import modules and packages
from cryptography.fernet import Fernet
import base64
import cowsay
import csv
import tabulate
import sys
import os
import time
import random
import re
from fpdf import FPDF

# Declare an Empty List
User_Names = []
User_NamesL = []

# List affirmation variables
affirmation_L = ["1", "y", "yes", "k", "ok", "okay", "okey"]

# List Quote opening
quote_L = [
    "Go For it",
    "Never Stop!",
    "The sky is your limit",
    "Awsome!",
    "What a day!",
    "CS50 Rocks",
    "Bright",
    "Vibrant",
    "I smell success",
    "Do Hard Things",
    "Be Strong",
    "Nothing is impossible",
    "Dream BIG",
    "Upward & Forward",
]

#
# Create or import master key to decrypt and encrpt files
#

# Create empty files list to store files in current directory
files = []

# Collect all files in user's current directory and store it in files list
for file in os.listdir():

    # Check if the file is not a folder
    if os.path.isfile(file):

        # Collect files
        files.append(file)

# Check if the masterkey is already exist. If so import the key. If not create one.
if ".thekey.key" not in files:
    key = Fernet.generate_key()
    with open(".thekey.key", "wb+") as thekey:
        thekey.write(key)
else:
    with open(".thekey.key", "rb") as thekey:
        key = thekey.read()


# Main function is started


def main():
    # Update the system
    try:
        decrypt_file("User_Data.txt")
        with open("User_Data.txt", "r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                User_Names.append(data)
        encrypt_file("User_Data.txt")
        # print(User_Names)
    except FileNotFoundError:
        pass

    # list already registered User names
    for Users in User_Names:
        User_NamesL.append(Users["User_Name"])

    # Prompt for user's User Name
    user_name = input("User Name: ")

    # Validate User Name
    valid = False
    while valid == False:
        valid = validate(user_name)

    # Make user's day with one of qoutes chosen randomly
    print()
    print("****Your Quote*****")
    print("-" * 35)
    time.sleep(0.5)
    print("          ", end="")
    print(random.choice(quote_L))
    time.sleep(0.5)
    print("_" * 35)
    print()
    print()

    # Take command
    while True:
        cmd = input("Command? (g-GoToMyDashboard e-Exit) > ")
        if cmd == "g":
            User_Function(user_name)
        elif cmd == "e":
            Exit_program()


# Function to validate the user name
def validate(user_name):

    # Register new User Name if the user is new
    if user_name not in User_NamesL:
        if (
            input("\nUser Name not found!!!\nCreate New user? (Y/N) ").lower()
            in affirmation_L
        ):
            user_pw = input("Input password: ")
            while True:
                if user_pw == input("Confirm password: "):
                    User_Names.append({"User_Name": user_name, "PassWord": user_pw})
                    return True
                else:
                    print("Password unmatched. Try again latter")
                    return False
        else:
            print("Operation canceled! ")
            sys.exit("Try again latter")

    # If the user exists, verify the user with password
    else:
        for user in User_Names:
            if user["User_Name"] == user_name:
                i = 3
                while i > 0:
                    if input("Password: ") == user["PassWord"]:
                        return True
                    else:
                        i -= 1
                        print(f"Incorrect password!!! {i} trial left")
                exit("too many trial")


def encrypt_file(FileName):
    try:
        with open(FileName, "rb") as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(FileName, "wb") as file:
            file.write(encrypted)

    except FileNotFoundError:
        # print(f"{FileName} not found")
        pass


def decrypt_file(FileName):
    try:
        with open(FileName, "rb") as file:
            data = file.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open(FileName, "wb") as file:
            file.write(decrypted)

    except FileNotFoundError:
        # print(f"{FileName} not found")
        pass
    # return decrypted


# Function to save changes and exit out of the program
def Exit_program():

    # Save the User Name and Password for next use
    decrypt_file("User_Data.txt")
    with open("User_Data.txt", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["User_Name", "PassWord"])
        writer.writeheader()
        for i in range(len(User_Names)):
            writer.writerow(User_Names[i])
    encrypt_file("User_Data.txt")

    # Exit the program
    cowsay.tux("Chao")
    sys.exit(0)


# Function for the verified user
def User_Function(user_name):

    # Declare new empty dictionary and list
    userAfileD = {}
    userAfile = []

    # Open user contact information file
    try:
        decrypt_file(user_name)
        with open(user_name, "r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                userAfile.append(data)
                userAfileD[data["Name"]] = data["Number"]
        encrypt_file(user_name)
        # userAfileL = [users_["Name"] for users_ in userAfile]
        # userAfileD = {users_["Name"]: users_["Number"] for users_ in userAfile}
    except FileNotFoundError:
        pass

    # Class for the user
    class User:

        # Define user
        def __init__(self, user_name):
            self.name = user_name
            """
            self.expimp
                self.expimp.export_contact
                self.expimp.import_contact
            Encrypting file is pending
            """

        # str name returns the name of the user
        def __str__(self):
            return self.name

        def get_numb():
            while True:
                numb = input("Number: ")
                numb = re.search("^((?:\+[0-9]{1,3})?[0-9]+)$", numb)
                if numb:
                    return numb.group(1)
                else:
                    print("Please enter only numbers\n Eg 09001102\n or Eg +2519001102")

        # Calling the user name
        @property
        def name(self):
            return self.name

        # Create new contact
        def create_new_contact(userAfileD):
            input_ = input("New Contact Name: ")

            # Check if the user already exists
            if input_ in userAfileD:
                print(f"Contact already exist!! {input_}: {userAfileD[input_]}")

                # Update an existing contact if the user requested
                if input("Do you want to change it? (Y/N) > ").lower() in affirmation_L:
                    new_name = input_
                    # new_numb = input("Number: ")
                    new_numb = user.get_numb()
                    if (
                        input(
                            f"Are you sure you want to change {new_name} number to {new_numb}? (Y/N) "
                        ).upper()
                        == "Y"
                    ):
                        userAfileD[new_name] = new_numb
                        print("Contact Updated! ")
                    else:
                        print("Operation haulted!!! ")

                # Cancel operation if input if wrong
                else:
                    print("Operation haulted!!! ")

            # Create new contact if the contact if new
            else:
                new_name = input_
                # new_numb = input(f"{new_name}\n Input Number: ")
                new_numb = user.get_numb()
                if (
                    input(f"Are you sure to save {new_name}: {new_numb} (Y/N) ").lower()
                    in affirmation_L
                ):
                    # userAfile.append({"Name": new_name, "Number": new_numb})
                    userAfileD[new_name] = new_numb
                    print("Contact Created! ")
                    # userAfileL.append(new_name)
                else:
                    print("Operation haulted!!! ")

        # Update an existing contact
        def update_e_contact(userAfileD):
            new_name = input("Name: ")

            # Check if the contact exists
            if new_name not in userAfileD:

                # Create the contact if it is new
                if (
                    input(
                        f"{new_name} not found in your contacts!!!\n Would you like to create new one? (Y/N) "
                    ).lower()
                    in affirmation_L
                ):
                    # new_numb = input(f"{new_name}\n Number: ")
                    new_numb = user.get_numb()
                    userAfileD[new_name] = new_numb
                    print("Contact Created! ")

                # Hault the operation if the input is wrong
                else:
                    print("Operation haulted!!! ")

            # Update the existing contact
            else:
                # new_numb = input(f"{new_name}\n Number: ")
                new_numb = user.get_numb()
                userAfileD[new_name] = new_numb
                print("Contact Updated! ")

        # List all contacts
        def list_all_contacts(userAfile):
            return tabulate.tabulate(userAfile, headers="keys", tablefmt="grid")

        # Find contact by name for the user
        def by_name(userAfileD):
            input_ = input("Name: ")
            if input_ in userAfileD:
                print(f"Name: {input_} ----- Phone number: {userAfileD[input_]}")
            else:
                print(f"Name does not exist\n type 'l' to list all your contacts")

        # Find contact by number for the user
        def by_numb(userAfileD):
            flagF = False
            input_ = input("Number: ")
            for users in userAfileD:
                if userAfileD[users] == input_:
                    print(f"Number: {input_} ----- Name: {users}")
                    flagF = True
            if flagF == False:
                print("Number not found!!!\n type 'l' to list all your contacts ")

        # Delete a contact
        def one_file(userAfileD):
            input_ = input("Name to DELETE: ")
            if input_ in userAfileD:
                if (
                    input(f"ARE YOU SURE TO DELETE {input_}??? (Y/N) ").lower()
                    in affirmation_L
                ):
                    userAfileD.pop(input_)
                    print("Contact Deleted! ")
                else:
                    print("Operation haulted!!! ")
            else:
                print(f"{input_} not found in your contacts")

        # Delete all of the contacts
        def all_file(userAfileD):
            if (
                input(
                    "ALL YOUR CONTACTS WILL BE DELETED\n Type 'DELETE ALL FILE' in cap letter to continue: "
                )
                == "DELETE ALL FILE"
            ):
                while len(userAfileD) > 0:
                    for users_ in userAfileD:
                        userAfileD.pop(users_)
                        break
                print("Contacts Deleted! ")
            else:
                print("Operation haulted!!! ")

        # Exit the function by saving changes
        def exit_program(userAfileD):
            decrypt_file(user_name)
            with open(user_name, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Number"])
                writer.writeheader()
                for Users in userAfileD:
                    writer.writerow({"Name": Users, "Number": userAfileD[Users]})
            encrypt_file(user_name)

        # Export all the contact in a pdf file format for the user
        def export_to_pdf(ExportName="Untitled.pdf"):
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 20)
            pdf.cell(0, 10, f"Contact Name ----------------- Contact Number", ln=True)
            pdf.cell(0, 10, f" ", ln=True)
            pdf.set_font("Helvetica", "", 12)
            for users in userAfileD:
                pdf.cell(
                    0, 10, f"{users} ................... {userAfileD[users]}", ln=True
                )

            pdf.output(ExportName)
            print("Contact Exported! ")
            print(f"Exported as {ExportName}")

    #### THE PROGRAM FOR THE VERIFIED USER BEGINS ###
    # ....----....----....----....----....----....---#

    # Create an object for the user using User Class constructor
    user = User

    # Greet the user
    cowsay.tux(f"Hi {user_name}. Welcome! This are lists of commands you can do")

    # List options for the user
    while True:
        print()
        print("to update a contact ------------------------ 'u'")
        print("list all your contacts --------------------- 'l'")
        print("find your contact name or number ----------- 'f'")
        print("delete all or some of your contact --------- 'd'")
        print("exit from the program ---------------------- 'e'")
        print("export your contacts as pdf file ----------- 'x'")

        # Import the user data and update the system
        userAfile = [
            {"Name": users, "Number": userAfileD[users]} for users in userAfileD
        ]

        # Prompt the user for new command
        match input("\n What would you like to do? "):

            #
            # Handle the commands as per command of the user
            #

            # list contacts if what the user asked for is so
            case "l":
                print(user.list_all_contacts(userAfile))
                print()

            # Create or Update contact for the user if required by the user
            case "u":
                match input("e--UpdateExistingContact\n n--CreateNewContact\n > "):

                    # Update existing contact
                    case "e":
                        user.update_e_contact(userAfileD)

                    # Create new contact
                    case "n":
                        user.create_new_contact(userAfileD)

            # Find a contact by name or number if required by the user
            case "f":
                match input("a--FindByName\n 0--FindByNumber\n > "):

                    # Find a contact by user's contact name
                    case "a":
                        user.by_name(userAfileD)

                    # Find a contact by user's contact number
                    case "0":
                        user.by_numb(userAfileD)

            # Delete contacts if the user required it
            case "d":
                match input("a--ToDeleteAllFile\n 1--ToDeleteOneFile\n > "):

                    # Delete all contacts for the user
                    case "a":
                        user.all_file(userAfileD)

                    # Delete one contact for the user
                    case "1":
                        user.one_file(userAfileD)

            # Exit from the program if user inquired it
            case "e":
                user.exit_program(userAfileD)
                Exit_program()

            # Export user's contact to pdf if the user wants it
            case "x":

                # Ask the user for the name of the pdf file to be exported to be called
                ExportName = input("What would you like to call your exported pdf? ")
                ExportName = f"{ExportName}.pdf"

                # Pass the user's contact for exporting the contacts
                user.export_to_pdf(ExportName)


# Just main is called. Nothing new :)
if __name__ == "__main__":
    main()
