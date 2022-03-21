import hashlib
import time
import sys
import mariadb
import server.socket
import socket


#sets up mariadb
import mariadb
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306)

cur = conn.cursor()
#-------------------------------
#begin functions
#------------------------------

def findPos(mainput):
    #this will find the position of a username in the database, this will be used to verify
    #the secnum
    positionFound = False

def session()


def usernameFunction(mainput):
    users = cur.execute(
        "SELECT username FROM accounts.accounts"
    )
    for user in users:
        if user == mainput:
            userposition = findPos(user)
            return True,
    else:
        return False



def passFunction(mainput):
    passwords = cur.execute(
        "SELECT password FROM accounts.accounts"
    )
    for password in passwords:
        if password == mainput:
            passPosition = findPos(password)
            return True
    else:
        return False


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



def withdrawl(mainput):
    print('withdrawl' + mainput)

def bal():
    print('bal')
    #needs to call username and password function

def deposit(usr, pswrd, secnum):




def msgHandler(msg):
    #depending on the 1st letter(command) the string will be manipulated.
    msg = msg.split()
    command = msg[0]
    username = msg[1]
    password = msg[2]
    query = msg[3]
    if msg[4]:
        secnum = msg[4]
    if command == '1':
        (username, password, query)
    elif command == '2':
        verify(username, password, secnum)
    elif command == '3':
        withdrawl(username, password, query,)
    elif command == '4':
        deposit(username, password, query)
    elif command == '5':
        bal(username, password)