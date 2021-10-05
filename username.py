#username.py
import main
import time
import sys
import accounts
import f
#username checker.
def usrlogin(mainput):
    user = accounts.ky
    if f.hash(mainput) == user:
            return True, user
    elif f.hash(mainput) != user:
            return False
    else:
            print("usrlogin failure")

def usernameFunction(mainput):
    usernameSignin = True
    while usernameSignin:
        usernameSigninAttempts = 0
        if usrlogin(mainput) == True:
            main.userkey = True

