import time
from time import sleep
import json
import os
import os.path
from os.path import exists

def listtostring(s):
    str1 = " "
    return (str1.join(s))

start = input("""1: login
2: sign up
3: exit
=>""")
if start == '3':
    quit()
elif start == '2':
    username = input("What would you like your username to be? ")
    password = input("Input your password ")
    if len(username) >= 21:
        print("Usernames can only be 20 letters long")
        quit()
    elif len(username) <= 2:
        print("Usernames cant be shorter than 3 characters")
        quit()
    if os.path.exists(f"Data/{username}.txt") == False:
        with open(f"Data/{username}.txt", 'w') as f:
            f.write(password)
    elif os.path.exists(f"Data/{username}.txt") == True:
        print("That user name already exists!")
        quit()
elif start == '1':
    user = input("What is your username? ")
    password = input("What is your password? ")
    if os.path.exists(f"Data/{user}.txt") == True:
        with open(f"Data/{user}.txt", 'r') as d:
            m = d.readlines()
            x = listtostring(m)
            if x == password:
                print("Logged in!")
            else:
                print("Invalid password!")
    elif os.path.exists(f"Data/{user}.txt") == False:
        print("Invalid username!")

else:
    print("Invalid option!")
    quit()