import hashlib
import time
import sys
import random
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

def sessionCreator():
    done = False
    counter = 0
    session = str
    while done == False:
        if len(counter) != 9:
            num = random.random()
            session = session + str(num)
            counter = counter + 1
        elif len(counter) < 9:
            #checks to see if the session id is already in the current database
            sessions = cur.execute("SELECT ssn FROM sessions")
            for ssn in sessions:
                if ssn == session:
                    done = False
                else:
                    done = True
                    server.socket.sessions(session)
                    continue
        return session


def signin(username, password, secnum):
    while attemptcounter <4:
        pCheck = cur.execute("SELECT password From accounts where username='" + username + "';")
        if password == pCheck:
            UserSession = sessionCreator()
        elif password != pCheck:
            attemptcounter + 1
            return 'wrong'


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
    print('verify not setup' + secnum)

def transfer(session, secnum, user, amount):
    print('hi')
    #send a notification to someone

def withdrawal(session, secnum, amount):
    print('')

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
    msg = msg.spplit()
    if messagesSent == 1:
        username = msg[1]
        password = msg[2]
        userCreator(username, password)
    else:
        command = msg[1]
        secnum = msg[2]
        session = msg[3]
        userCommand = msg[4]
        #continue search
        if command == '1':
            withdrawal(session, secnum)
        elif command == '2':
            deposit(session)
        elif command == '3':
            bal(session, secnum)
        elif command == '4':
            transfer(session, secnum)