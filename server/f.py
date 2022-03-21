import hashlib
import time
import sys
import random
import mariadb
import server.socket
import socket


#sets up mariadb
import mariadb
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
    )

cur = conn.cursor()
#-------------------------------
#begin functions
#------------------------------

def findPos(mainput, type):
    cur.execute(
        f"SELECT {type} FROM accounts.accounts;"
    )
    variableFound = False
    while not variableFound:
        for variable in type:
            if variable == mainput:
                return variable
                variableFound = True
            else:
                None
    positionFound = False

def sessionCreator(userpos, passpos):
    print('session')


def usernameFunction(mainput):
    users = cur.execute(
        "SELECT username FROM accounts.accounts"
    )
    for user in users:
        if user == mainput:
            userposition = findPos(user, 'username')
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
def verify(secnum):
    print('verify not setup' + mainput)



def withdrawl(mainput):
    print('withdrawl' + mainput)

def bal():
    print('bal')
    #needs to call username and password function

def deposit(usr, pswrd, secnum, amount):
    if verify(secnum):
        cur.execute(
        ""
            )
#-----------------------
#figure out how to store a variable that is equal to
#the position of the username and password provided
#in the database





def userCreator(username, password, secnum):
    cur.execute(
    "INSERT INTO accounts(username, password, secnum) VALUES ('" + username + "', '" + password + "', '" + int(secnum) + "');"
    )
    conn.commit()


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
    elif command == '5':
        userCreator(username, password, secnum)