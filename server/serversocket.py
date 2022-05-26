from genericpath import exists
import hashlib
from ssl import SSLSession
import time
import sys
import random
import datetime
import threading
from tkinter import Y
import mariadb
import re
import string
import socket

#if it doesnt work you need to pip install mariadb :)

connected = bool
# waits for client to connect, and then
# establishes a fluid socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
header = 64
cHeader = 2048
port = 3305
server =  socket.gethostbyname(socket.gethostname())
addr = (server, port)
format = 'utf-8'
disconnect_message = '!disconnect'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)

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

def logEnable(param):
    today = datetime.date.today()
    todayinfo = today.strftime("%d%m%Y")
    global logfilename
    if param != '':
        logfilename = (param + str(todayinfo) + '.txt')
    elif param == '':
        logfilename = ('bankSystemLog-' + str(todayinfo) + '.txt')
    print("Logging enabled at filename: " + logfilename)
    return logfilename



def log(inp):
    print(inp)
    #creates a log file with the date, and time
    global logfilename 
    f = open(str(logfilename), "a")
    f.write("\n" + inp)
    f.close

def error():
    log("\n[Server] : Sent Error Message.")
    return 'error'


def sessionCreator(username):
    counter = 0
    session = ''
    attempts = 1
    working = True
    while working:
        if counter < 9:
            num = random.randint(0, 9)
            session = session + str(num)
            counter = counter + 1
            continue
        if counter == 9:
            cur.execute("SELECT sessionID FROM sessions WHERE sessionID=" + session)
            seshchecker = cur.fetchone()
            seshchecker = str(seshchecker)
            print(f"seshchecker: {seshchecker}")
            if seshchecker != 'None':
                attempts = attempts + 1
                session = ''
                counter = 0
                continue
            elif seshchecker == 'None':
                sql = "INSERT INTO sessions (sessionID, username) VALUES (?, ?)"
                data = (session, username)
                cur.execute(sql, data)
                conn.commit()
                print(f"commited, {data}. It took {attempts} attempts.")
                break


#creates a secnum for nem users
def secnumCreator(sec):
    counter = 0
    secnum = ''
    attempts = 1
    while True:
        if counter < 9:
            num = random.randint(0, 9)
            secnum = secnum + str(num)
            counter = counter + 1
            continue
        elif counter == 9:
            cur.execute("SELECT secnum FROM bankSystem WHERE secnum=" + secnum + ";")
            secnumchecker = cur.fetchone()
            secnumchecker = str(secnumchecker)
            if secnumchecker != 'None':
                continue
                attempts = attempts + 1
            elif secnumchecker == 'None':
                log("Created secnum : " + str(secnum) + ", took " + str(attempts) + " attempts.")
                return secnum 

def userCreator(username, password, secnum):
    #checks the secnum
    if secnum == '' or len(str(secnum)) != 9:
        secnum1 = secnumCreator(username)
        created = True
    elif len(str(secnum)) == 9:
        secnum1 = secnum
        created = False
    sql = "INSERT INTO bankSystem (username, password, secnum) VALUES (?, ?, ?)"
    data = (username, password, secnum1)
    cur.execute(sql, data)
    conn.commit()
    if created:
        log(f"created account {str(username).title()}. Created the secnum {str(secnum1)} for the account.")
    elif not created:
        log(f"created account {str(username).title()}. With the secnum: {str(secnum1)}")
    return True

# hasher
def hasher(hashInput):
    return str(hashlib.sha256(str(hashInput).encode('utf-8')).hexdigest())


def verify(sesh, sec):
    cur.execute("SELECT username FROM sessions WHERE sessionID='" + sesh + "';")
    sessionCheck = cur.fetchone()
    cur.execute("SELECT username FROM bankSystem WHERE secnum ='" + sec + "';")
    accountsCheck = cur.fetchone()
    if str(sessionCheck) == str(accountsCheck):
        return True
    elif str(sessionCheck) != str(accountsCheck):
        return False


def verifyUser(usr):
    cur.execute("SELECT username FROM bankSystem WHERE username='" + usr + "';")
    usrcheck = cur.fetchone()
    if usrcheck == 'None':
        return True
    if usrcheck != 'None':
        return False

#=============== COMPELTE CODE LINE ==========================================
#everything below this line is not completely checked, and needs to be checked! :D

def strip(param):
    paramstr = str(param)
    PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
    answer = "".join(c for c in paramstr if c in PERMITTED_CHARS)
    return answer

#checks that the password correlated to the entered username is correct.
def verifyLogin(usr, pwd):
    if verifyUser(usr):
        cur.execute("SELECT password FROM bankSystem WHERE username='" + str(usr) + "';")
        sqlpwd = cur.fetchone()
        if sqlpwd == pwd:
            return True
        elif sqlpwd != pwd:
            return False

def withdrawal(sesh, sec, amount):
    if verify(sesh, sec):
        cur.execute("SELECT username FROM sessions WHERE sessionID=" + sesh + ";")
        username = cur.fetchone()
        username = str(username)
        username = strip(username)
        cur.execute("SELECT bal FROM bankSystem WHERE username='" + username + "';")
        currentBal = cur.fetchone()
        currentBal = strip(currentBal)
        oldBal = currentBal
        currentBal = int(currentBal) - int(amount)
        currentBal = str(currentBal)
        cur.execute("UPDATE bankSystem SET bal=" + currentBal + " WHERE username='" + username + "';")
        conn.commit()
        cur.execute("SELECT bal FROM bankSystem WHERE username='" + username + "';")
        check = cur.fetchone()
        check = strip(check)
        if check == currentBal:
            log(f"Updated {username.title()} balance from {oldBal} to {currentBal}.")
            return f"Updated {username.title()} balance from {oldBal} to {currentBal}."
        elif check != currentBal:
            log(f"error.")
            return f"error."

def bal(sesh, sec):
    if verify(sesh, sec):
        print('verified, '+ sesh + ', ' + sec)
        cur.execute("SELECT bal FROM bankSystem WHERE secnum='" + sec + "';")
        balance = cur.fetchone()
        balance = strip(balance)
        log(f"User: {sesh} requested balance, recieved: {balance}")
        return f"User: {sesh} requested balance, recieved: {balance}"
    else:
        return "error"


def sessionEnder(username):
    cur.execute("DELETE FROM sessions WHERE username='" + username + "';")
    conn.commit()
    return True


def deposit(sesh, secnum, amount):
    complete = bool
    if verify(sesh, secnum):
        cur.execute("SELECT bal FROM bankSystem WHERE secnum=" + secnum + ';')
        bal = cur.fetchone()
        bal = strip(bal)
        newBal = int(bal) + int(amount)
        newBal = str(newBal)
        cur.execute("UPDATE bal FROM bankSystem WHERE secnum=" + secnum + ";")
        conn.commmit()
        check = cur.execute("SELECT bal FROM bankSytem WHERE secnum="  + secnum + ';')
        check = strip(check)
        if check == newBal:
            log(f"Changed balance of {sesh} from {bal} to {check}")
            return f"Changed balance of {sesh} from {bal} to {check}"
        elif check != newBal:
            log(f"[FAILED]: Changing balance of {sesh} from {bal} to {check}.")
            return f"[FAILED]: Changing balance of {sesh} from {bal} to {check}."

# ------------------------------

messagesSent = 1


def msgHandler(mesg): 
    # depending on the 1st letter(command) the string will be manipulated.
    msg = mesg.split()
#create new functoion where 1 is requesting a session from a already logged user
#2 is creating an account
#3 is checking if the username is available
#4-7 take the previous sequence, with section one being command, section 2 being
#usrcmd, section 3 being session, section 4 being secnum
    if int(msg[0]) == 1 or 2 or 3:
        command = msg[0]
        username = msg[1]
        password = msg[2]
        secnum = msg[3]
        if command == '1':
            if verifyLogin(username):
                func = sessionCreator(username)
                return(func)
            else:
                return("Failed to verify username.")
        elif command == '3':
            vUser = verifyUser(username)
            return(str(vUser))
        elif command == '2':
            var = userCreator(username, password, secnum)
            return(var)
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
            return('error')
        #when ready add a transfer function.
    elif msg[1] == disconnect_message:
        if sessionEnder(msg[2]):
            cur.execute("DELETE FROM sessions WHERE username=?", msg[2])
    else:
        return('error')


#handles socket clients
def handle_client(connection, address):
    log(f"[new connection]: " + str(address) + " has connected.")
    connected = True
    while True:
        if connected:
            msg = connection.recv(header).decode(format)
            log(f"[{address}]: '{str(msg)}'")
            msg = msg.rstrip()
            print("stripped: ..." + msg + "....")
            h = msgHandler(msg)
            connection.send(bytes(h.encode(format)))
            log(f'[{str(address)}]: sent: "{msg}" | returned:"{str(h)}"')
            break
        else:
            continue
    connection.close()


#starts the server
def start():
    #queries user to log
    logQ()
    #listens for connections
    s.listen()
    log(f"Server is listening on '{str(server)}:{str(port)}'.")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        log(f"[connections] : {threading.active_count() - 1}")
        

def logQ():    
    while True:
        logQ = input("Would you like the server to log to a file?")
        if logQ.lower() == 'yes' or 'y':
            logQ2 = input("What would you like to name the file? (We'll include the date for you)(Press ENTER to skip) ")
            logEnable(logQ2)
            print("Started logging at " + str(datetime.datetime.now()))
            break
        elif logQ.lower() == 'no' or 'n':
            print("Okay, continuing.")
            break
        else:
            print("Improper syntax, try again with 'yes', or 'no'")
            continue
#starts the main server listener
start()