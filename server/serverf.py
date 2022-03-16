import hashlib
import time
import sys


# functions "class'" for servermain.py developed by grizhe


# this entire section needs to be reviewed, as accounts.ky does not exist any longer.
# update this section once you have completed the server socket implimentations
# and the serveraccount / database implementations.


def toomanyattempts(reason):
    print("Program shutting down due to too many attempts, reason:")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()


# hasher
def hasher(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest())


def disband(reason):
    print("Program shutdown via internal kill switch.")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(3)
    sys.exit()

    # Account Number Verification
def verify(mainput):
    print('verify not setup' + mainput)


# username stuff
def usrlogin(mainput):
    # ====
    print('usrlogin not setup' + mainput)


def usernameFunction(mainput):
    print('usernameFunction not setup' + mainput)


# password stuff
def passFunction(mainput):
    print('passFunction not setup' + mainput)
