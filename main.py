#main.py
import accounts
import f
import hashlib
import sys
import time
import username

userkey = False
passkey = False
seckey = False
acnum = False
while True:
    while True:
        if userkey == True:
            continue
        else:
            inp1 = input("Welcome, please type your username.")
            f.usernameFunction(str(inp1))
            print("Welcome, " + accounts.ky[name] + ". Please enter your password:"
            inp2 = input("")
            f.passfunction(inp2)
