import hashlib
import time
import sys
import random
import mariadb
import socket


attemptcounter = 1
# sets up mariadb
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
)

cur = conn.cursor()


# -------------------------------
# begin functions
# ------------------------------


def sessionCreator(username):
    counter = 0
    session = ''
    while True:
        if counter < 9:
            num = random.randint(0, 9)
            session = session + str(num)
            counter = counter + 1
            continue
        elif counter == 9:
            cur.execute("INSERT INTO sessions (sessionID, username) values ('" + session + "', '" + username + ");")
            serversocket.send('1 ' + str(session))
        return True

#creates a secnum for nem users
def secnumCreator(sec):
    counter = 0
    secnum = ''
    while True:
        if counter < 9:
            num = random.randint(0, 9)
            secnum = secnum + str(num)
            counter = counter + 1
            continue
        elif counter == 9:
            return secnum


def userCreator(usr, pwd):
    # scans for the username
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
            cur.execute("INSERT INTO sessions(sessionID, secnum) values ('" + sesh + "', '" + secnum + "');")
            serversocket.send(str(sesh) + ' ' + str(secnum))
    if error:
        return False


# hasher
def hasher(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest())


def verify(sesh, sec):
    sessionAttempt = cur.execute("SHOW username FROM sessions WHERE sessionID='" + sesh + "';")
    accountAttempt = cur.execute("SHOW username FROM accounts WHERE secnum ='" + sec + "';")
    if sessionAttempt == accountAttempt:
        return True
    else:
        return False

def verifyUser(usr):
    try:
        username = cur.execute(
        "SHOW username FROM accounts WHERE username='" + usr + "';"
    )
    except Exception as e:
        print(str(e))
    try:
        password = cur.execute(
        "SHOW password FROM accounts WHERE username='" + usr + "';"
    )
    except Exception as e:
        print(str(e))
    if e:
        return False
    else:
        return True

def withdrawal(sesh, sec, amount):
    if verify(sesh, sec):
        currentAmount = cur.execute("SELECT bal FROM accounts WHERE secnum='" + sec + "';")
        newAmount = int(currentAmount) - int(amount)
        cur.execute("UPDATE accounts SET bal = '" + newAmount + "' WHERE secnum=" + sec + "';")
        test = cur.execute("SELECT bal FROM accounts WHERE secnum='" + sec + "';")
        if test == newAmount:
            return True
        else:
            return


def bal(sesh, sec):
    if verify(sesh, sec):
        balance = ("SELECT bal FROM accounts WHERE secnum='" + sec + "';")
        return balance
    else:
        return None


def sessionEnder(username):
    try:
        cur.exeucte(
        "DELETE FROM sessions WHERE username='" + username + "';")
    except Exception as e:
        print('')
    if not e:
        return True
    if e:
        return False

def deposit(sesh, secnum, amount):
    complete = bool
    if verify(sesh, secnum):
        currentAmount = cur.execute("SELECT bal FROM accounts WHERE secnum='" + secnum + "';")
        combinedAmount = int(currentAmount) + int(amount)
        cur.execute(
            "UPDATE accounts SET bal = '" + combinedAmount + "' WHERE secnum='" + secnum + "';"
        )
        checkAmount = cur.execute("SELECT bal FROM accounts WHERE secnum='" + secnum + "';")
        if checkAmount == combinedAmount:
            return str(checkAmount)
        else:
            cur.execute(
                "UPDATE accounts SET bal = '" + currentAmount + "' WHERE secnum='" + secnum + "';"
            )


# -----------------------
# figure out how to store a variable that is equal to
# the position of the username and password provided
# in the database


def userCreator(username, password, secnum):
    cur.execute(
        "INSERT INTO accounts(username, password, secnum) VALUES ('" + username + "', '" + password + "', '" + int(
            secnum) + "');"
    )
    conn.commit()


messagesSent = 1


def msgHandler(msg):
    # depending on the 1st letter(command) the string will be manipulated.
    msg = msg.split()
#create new functoion where 1 is requesting a session from a already logged user
#2 is creating an account
#3 is checking if the username is available
#4-7 take the previous sequence, with section one being command, section 2 being
#usrcmd, section 3 being session, section 4 being secnum
    if int(msg[0]) == 1 or 2 or 3:
        command = msg[0]
        username = msg[1]
        password = msg[2]
        if command == '1':
            if verifyUser(username):
                serversocket.send(sessionCreator(username))
        elif command == '3':
            if verifyUser(username):
                serversocket.send('good')
            else:
                serversocket.send('ngod')
        elif command == '2':
            userCreator(username, password)
    elif int(msg[1]) == 4 or 5 or 6:
        command = msg[1]
        usrcmd = msg[2]
        session = msg[3]
        secnum = msg[4]
        if command == '1':
            withdrawal(session, secnum, usrcmd)
        elif command == '2':
            bal(session, secnum)
        elif command == '3':
            deposit(session, usrcmd)
        else:
            serversocket.send('error')
        #when ready add a transfer function.
    elif msg[1] == serversocket.disconnect_message:
        if sessionEnder(msg[2]):
            cur.execute("DELETE FROM sessions WHERE username='" + str(msg[2]) + "';")
    else:
        serversocket.send('error')
