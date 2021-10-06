import hashlib
import sys
import accounts
import main
import time


def disband(reason):
    print("Program shutdown via internal kill switch.")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()


def toomanyattempts(reason):
    print("Program shutting down due to too many attempts, reason:")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()


def wip():
    print("This section of the code is known to be buggy and is a work in progress.")


# hasher
def hashFunction(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest)


# number encryption and decryption
def nuymencrypt(numinp):
    int(numinp)
    numinp + 1.45 - 3 / 6.2356622 * 3.543970 * 15.193241
    return numinp


def numdecrypt(mainput):
    int(mainput)
    mainput / 15.193241 / 3.543970 * 6.2356622 + 3 - 1.45


# username stuff
def usrlogin(mainput):
    user = str(accounts.ky.get('userhash'))
    if hashFunction(mainput) == user:
        return True, user
    elif hashFunction(mainput) != user:
        return False
    else:
        print("usrlogin failure")


def usernameFunction(mainput):
    usernameSigninAttempts = 0
    if usernameSigninAttempts == 3:
        print("You have tried too many times, and reached the limit of " + str(usernameSigninAttempts) + "/3 tries.")
        toomanyattempts("Username")
    while usernameSigninAttempts < 4:
        if usrlogin(mainput):
            main.userkey = True
        elif not usrlogin(mainput):
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

#Account Number Verification
def accountNumberVerifier(mainput):
    if str(mainput) == accounts.ky.get('accountnum'):
        return True
    elif str(mainput) is not accounts.ky.get('accountnum'):
        print("Account number not matched, recieved: " + str(mainput) + ", instead of " + str(accounts.ky.get('accountnum')) + ".")
        return False