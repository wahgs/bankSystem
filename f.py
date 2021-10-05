#lets hope this works
import hashlib
import accounts
import sys
import main


def disband():
    print("Program shutdown via internal kill switch.")
    sys.exit()

def wip():
    print("This section of the code is known to be buggy and is a work in progress.")

def hash(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest)

#number encryption and decryption
def nuymencrypt(numinp):
    int(numinp)
    numinp + 1.45 - 3 / 6.2356622 * 3.543970 * 15.193241
    return numinp

def numdecrypt(mainput):
    int(numinp)
    numinp / 15.193241 / 3.543970 *6.2356622 + 3 - 1.45

#username stuff
def usrlogin(mainput):
    user = accounts.ky
    if hash(mainput) == user:
        return True, user
    elif hash(mainput) != user:
        return False
    else:
        print("usrlogin failure")

def usernameFunction(mainput):
    usernameSignin = True
    while usernameSignin:
        usernameSigninAttempts = 0
        if usrlogin(mainput) == True:
            main.userkey = True