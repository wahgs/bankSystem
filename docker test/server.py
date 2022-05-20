import socket
import hashlib
import mariadb
import threading
import datetime
import string

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
header = 2048
port = 3305
server =  socket.gethostbyname(socket.gethostname())
addr = (server, port)
format = 'utf-8'
disconnect_message = '!disconnect'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)

attemptcounter = 1
# sets up mariadb
connmaria = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
)

cur = connmaria.cursor()

#================================================
logfilename = ('testlog-' + '.txt')


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
        secnum = secnum
        not created
    sql = "INSERT INTO bankSystem (username, password, secnum) VALUES (?, ?, ?)"
    data = (username, password, secnum1)
    cur.execute(sql, data)
    conn.commit()
    if created:
        log(f"created account {str(username).title()}. Created the secnum {str(secnum1)} for the account.")
    elif not created:
        log(f"created account {str(username).title()}. With the secnum{str(secnum1)}")
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
            return True
        elif check != currentBal:
            print('error...')
            return False

def bal(sesh, sec):
    if verify(sesh, sec):
        print('verified, '+ sesh + ', ' + sec)
        cur.execute("SELECT bal FROM bankSystem WHERE secnum='" + sec + "';")
        balance = cur.fetchone()
        balance = strip(balance)
        log(f"User: {sesh} requested balance, recieved: {balance}")
        return balance
    else:
        return None


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
            return True
        elif check != newBal:
            log(f"[FAILED]: Changing balance of {sesh} from {bal} to {check}.")
            return False

# ------------------------------

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
        secnum = msg[3]
        if command == '1':
            if verifyUser(username):
                return(sessionCreator(username))
        elif command == '3':
            if verifyUser(username):
                return('good')
            else:
                return('nope')
        elif command == '2':
            userCreator(username, password, secnum)
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


inp = input('Input: ')
msgHandler(inp)