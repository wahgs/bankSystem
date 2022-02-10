import hashlib
import time
import sys
import socket
import serversocket

#functions "class'" for servermain.py developed by grizhe

def toomanyattempts(reason):
    print("Program shutting down due to too many attempts, reason:")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()

# hasher
def hashFunction(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest())

def disband(reason):
    print("Program shutdown via internal kill switch.")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()

#Account Number Verification
#/def accountNumberVerifier(mainput):
    if str(mainput) == accounts.ky.get('accountnum'):
        return True
    elif str(mainput) is not accounts.ky.get('accountnum'):
        print("Account number not matched, recieved: " + str(mainput) + ", instead of " + str(accounts.ky.get('accountnum')) + ".")
        return False

# username stuff
def usrlogin(mainput):
    user = str(accounts.ky.get('userhash'))
    if hashFunction(mainput) == user:
        return True, user
    elif mainput is user:
        return True, user
    elif hashFunction(mainput) != user:
        return False
    else:
        print("serverf.usrlogin failure")

def usernameFunction(mainput):
    usernameSigninAttempts = 0
    if usernameSigninAttempts == 4:
        print("You have tried too many times, and reached the limit of " + str(usernameSigninAttempts) + "/3 tries.")
        toomanyattempts("Username")
    while usernameSigninAttempts < 4:
        if not usrlogin(mainput):
            int(usernameSigninAttempts) + 1
            print("Incorrect password, Please try again. Attempt " + str(usernameSigninAttempts) + "/3.")
        else:
            print("usernameFunction error in f.py")

# password stuff
def passFunction(mainput):
    passAttempts = 0
    mainputHashed = str(hashFunction(mainput))
    while passAttempts < 4:
        if passAttempts == 3:
            print("You have tried too many times, and reached the limit of " + str(passAttempts) + "/3 tries.")
            toomanyattempts("Password")
            return False
        else:
            if mainputHashed == str(accounts.ky.get('password')):
                return True
            elif mainputHashed != str(accounts.ky.get('password')):
                int(passAttempts) + 1
                print("Attempt " + str(passAttempts) + "/3. Please try again. (CaSe Sensitive)")
                continue
