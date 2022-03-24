import hashlib
import time
import sys
import random
import mariadb
import serversocket
import socket
import serversocket

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
        return str(session)

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
    try:
        password = cur.execute(
        "SHOW password FROM accounts WHERE username='" + usr + "';"
    )
    except Exception as e:
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
    if messagesSent == 1:
        logOrCreate = msg[0]
        username = msg[1]
        password = msg[2]
        if logOrCreate == '1':
            if verifyUser(username):
                main.send(sessionCreator(username))
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
        # add when ready add a transfer function.