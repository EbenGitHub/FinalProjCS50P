# Final Project for CS50P Course


## About the creater
![This is an image](https://ca.slack-edge.com/T0195LMKD1R-U032HH8BPJS-0ef672957214-48)
Hi!! My Name is Abenezer Eshetie aka Ebenezer Eshexie. I am from Ethiopia, Eastern Africa. I am self-taught software developer and web designer. I am one of CS50 virtual student. I enjoy coding for fun but i have got to admit that this is my first time to code over 500 lines of codes. I learnt alot through it. Yea. But the point is to apply most of thing i learnt here. It was fun. You have fun too by playing with the program. See you soon! :)

## What the program is
The program is multi-user enabled contact saver. With different user accounts, it can store as much contacts as the user wants without user information mixing with eachother.

## How to use it
Hold on! Wait a minute.
1. Before anything, you need to install the required python packages for the program to run with out any error. The steps are as follows:
* Go to final project directory using _'cd'_ command.
* Run the following command _'pip install -r requirements.txt'_
* If you can go to requirements.txt and install eack packages one by one using the following command _'pip install [package]'_
2. Nice. Now you can run the program using the following command _'python final.py'_
3. You will be prompt for __User Name__. Just Input your User Name. Don't worry. The program will know that you are new user and will prompt you if you want to create one.
* If you want to create new user, input _'y'_ or any of the following commands:
> _'1'_  _'y'_  _'yes'_  _'k'_  _'ok'_  _'okay'_  _'okey'_  in Caps Lock on or off or even mixed.
* Any key that is not in the above list will abort the operation.
* Input you new user password
* Confirm the exact password you typed. Other wise you will be re-prompt if you want to create new user.
4. If you already have user name, then when you input your user name, you will be asked for password. The program shuts down with 3 incorrect trial for the password.
5. Wow. you are in. Now you should see beautuful qoute to make your day. You should also see a prompt waiting for your command. Go ahead and 
* Input - _'g'_ to go to your user dashboard.
* Input - _'e'_ to exit out of the program. Any key input other than this will make to re-prompt your for correct input.
6. If you went to dashboard, BOOOOM. You should see a penguin greeting you by your user name and list of the commands you can use.
* Input - _'u'_ to update an existing contact or create a new one. This is the first function you should do to enjoy other commands.
 Now you are prompt for more clear command. 
> To update an existing contact, input _'e'_. Now you will be prompt for the name of contact and number. Enter accordingly. Oops. I forgot we don't have one. But try to put your contact name. Not what you expected huh? The program will know that the contact by that name does not exist and will prompt you if you want to create one. 
####
> To create new contact,  input _'n'_. Now you will be prompt for the name of contact and number. Enter accordingly. What if you entered the contact that already exist? Will it override it? Try it. Got you again huh? The program will know that the contact by that name already exists and will prompt you if you want to change the number of that contact.
####
> This is not only how smart the program gets. Okay try to create a new contact and input this _'1234f'_ when prompt for Number. Haha. You should see the program rejecting your input saying _"you should only input numbers"_. Okay try this _'+1747474'_. It accepts you even though all your inputs are not numbers. THIS IS JUST A BEGINNENIG OF THE FUN
* Now try to input - _'l'_ to to see the contacts you created. It should present you in a beautiful table.
* Now try to input - _'f'_ to find numbers or contact's name in your contact. 
####
> If you want to search contacts by the name of your contact's name, input - _'a'_. 
####
> If you want to search contacts by the number of your contact's number, input - _'0'_. __NOTE__ that it is not the letter "o", but the number "0" aka zero. It is kind of cool right.
* Input - _'d'_ to delete your contacts. 
####
> If you want to delete all of your contacts, input - _'a'_. That command means _'all'_, so becareful! 
####
> If you want to delete just one of your contact, input - _'1'_. Again __NOTE__ that it is not the letter "l", but the number "1" aka one. 
####
> If the name you provided does not exist in your contacts, the operation will abort with message "Name not found".
* Getting used to it? Cool!
* Input - _'e'_ if you want to save you contacts and exist from the program. If you interrupt the program, all your information you just entered will be lost.
* This is the final and exciting part of HOW TO USE. If you want to export your contacts as pdf, input - _'x'_.  Then enter the name of the pdf file you want it to be called __without extension__. Eg like _'mypdf'_ but not _'mypdf.pdf'_. The program will add the extension for you.
* THAT IS IT! GO AND PLAY WITH IT.
## Features of the program
* One benefit of the program is, it will register all your user information and contact informaion using File I/O. So next when you log, you will get all your saved contacts. Isn't that cool.
* Your user information including your user name and password will be stored in a file called _'User\_Data.txt'_ & all your contact information will be store in a file name by your user name. Ohh. Do that mean any user can see your user name, password and contacts? try _'cat User\_Data.txt'_. Huh. The program will automatically encrpt your file immediatly after usage. This is very tight security. Where is the key store? the key is in a file called _'thekey'_. Try _'ls'_. You don't see it right? Try _'ls -a'_. Now you see it as _'.thekey.key'_. Normal users won't see it. Don't tell this to anyone. This is a secrete between me and you. ;)
* The other awsome feature of this program is it will check if you input for a number is a real phone number when trying to save a contact. You can write phone numbers with only numbers or preceeded with plus sign and country code. You can't input other than this options. That is some serious check and data cleaning.

## Contact developer

If you have comments, or want to contribute to this program or by any means if you want to contact me, use:
- [x] GitHub User name: [Eenrics](https://github.com/Eenrics/)
- [x] Email Address: ebenezeresh525@gmail.com
- [x] Phone Number: +251955455616


## Aknowledgment
- Thank you [CS50 Harvard](https://cs50.harvard.edu/python/2022/)
- Thank you [David J. Malan](https://github.com/dmalan)
- Thank you all CS50 teams
- Thank you God


 >© Copyright Reserved! Kiding :) 
 >Use it. I don't care.
