from utils.ui import banner_small, clear
from utils.pwd import getpw, encrypt
from src.users import User
from utils.db import *
import os
import json


def login(username: str, pwd: str) -> bool:
    if f"{username}.json" in os.listdir("data/Users"):
        with open(f"data/Users/{username}.json", "r") as f:
            data = json.load(f)
        if encrypt(pwd) == data["password"]:
            print("Logged in succesfully")
            return True
        else:
            print("Wrong Password !")
    else:
        print("Username not found !")
    return False


def signup() -> bool:
    first_name = input("\nEnter your first name::\t").strip()
    last_name = input("\nEnter your last name::\t").strip()
    username = input("\nEnter your username::\t").strip()
    email = input("\nEnter your E-mail address::\t").strip()

    password = ""
    password_conf = " "
    while password_conf != password:
        password = getpw()
        password_conf = getpw(PROMPT="\nConfirm your password::\t")

    user = User(first_name, last_name, email, username, encrypt(password_conf))

    if add_user(user):
        print("User signup successful")
        return login(user.email, user.password)
    else:
        print("User generation failed.")
        return False


def check_login():
    check_login = int(
        input(
            "\n\t[1] Login \t\t [2] Sign Up \t\t [0] Exit \n\n \tEnter you choice::\t"
        )
    )

    if check_login == 1:
        clear()
        print(banner_small)
        print("Logging in...")
        return login(
            username=input("\nEnter your username::\t").strip(),
            pwd=getpw("\nEnter your password::\t"),
        )

    elif check_login == 2:
        clear()
        print(banner_small)
        print("Signing Up...")
        return signup()

    elif check_login == 0:
        clear()
        exit()

    else:
        clear()
        print(banner_small)
        print("Invalid Choice...")
        return 0
