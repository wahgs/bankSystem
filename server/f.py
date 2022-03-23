import hashlib
import time
import sys
import random
from typing_extensions import TypeVarTuple
import mariadb
import server.socket
import socket

attemptcounter = 1
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


def sessionCreator(username):
    done = False
    counter = 0
    session = ''
    while done == False:
        if counter < 9:
            num = random.randint(0,9)
            session = session + str(num)
            counter = counter + 1
            continue
        elif counter == 9:
            cur.execute("INSERT INTO sessions (sessionID, username) values ('" + session "', '" + username");")
        return session    


def userCreator(usr,pwd):
    #scans for the username
    usrCheck = bool
    pwdCheck = bool
    error = False
    users = cur.execute("SHOW username FROM accounts")
    while not error: 
        for user in users:
            if user == usr:
                error = True
                break
            else:
                continue
        if not error:
            usrCheck = True
        if usrCheck:
            sesh = sessionCreator(usr)
            secnum = secnumCreator(secnum)
            cur.execute("INSERT INTO accounts(username, password, secnum, bal) values ('" + usr + "', '"
+ pwd + "', '" + secnum + "', '0');")
            cur.execute("INSERT INTO sessions(sessionID, secnum) values ('" + sesh "', '" + secnum + "');")
    if error:
        return False

        
# hasher
def hasher(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest())

def verifier(sesh, sec):
    sessionAttempt = cur.execute("SHOW username FROM sessions WHERE sessionID='" + sesh + "';")
    accountAttempt = cur.execute("SHOW username FROM accounts WHERE secnum ='" + sec + "';")
    if sessionAttempt == accountAttempt:
        return True
    else:
        return False


def withdrawl(sesh, sec, amount):
    print('withdrawl' + mainput)

def bal(sesh, sec):
    print('bal')
    #needs to call username and password function

def deposit(sesh, secnum, amount):
    if verify(sesh, secnum):
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

messagesSent = 1
def msgHandler(msg):
    #depending on the 1st letter(command) the string will be manipulated.
    msg = msg.split()
    if messagesSent == 1:
        username = msg[1]
        password = msg[2]
        userCreator(username, password)
    elif messagesSent > 2:
        session = msg[1]
        secnum = msg[2]
        command = msg[3]
        usrcmd = msg[4]
        if command == '1':
            withdrawal(session, secnum, usrcmd)
        elif command == '2':
            bal(session, secnum)
        elif command == '3':
            deposit(session, usrcmd)
        #add when ready add a transfer function.
        
