from asyncio import wait_for
from lib2to3.pgen2 import token
from logging import exception
import socket
from time import sleep
import hashlib
import sys
from xmlrpc.server import ServerHTMLDoc

header = 2048
port = 3305
format = 'UTF-8'
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loggedIn = False
session = ''
secnum = ''


def help():
    print('[HELP] : List of commands:')
    print("IF YOU'RE LOGGED IN:")
    print('[deposit] : Will allow you to enter an amount to deposit into the account balance.')
    print('[withdrawal] : Will allows you to enter an amount to withdraw from the account balance.')
    print('[balance] : Will display the balance of the coordinated account')
    print("\n\nIF YOU'RE NOT LOGGED IN:")
    print('[login] : begins a login sequence that allows a user to login using their credentials.')
    print('[create]: begins a sequence for creating accounts that allows the user to create a bankSystem account.')
    print('[help]: shows all commands.')


#===================================-BEGIN USEFUL FUNCTIONS-=================================================
#hashes a string into a sha256 hash, then encodes in utf-8 :)
def hasher(inp):
    return(str(hashlib.sha256(str(inp)).encode(format)).hexdigest())

def checkSession():
    global session
    if session == '':
        return False
    else:
        return True


#strips a message of commas, etc. In order to avoid injection, sloppiness, etc.
def strip(param):
    paramstr = str(param)
    PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
    answer = "".join(c for c in paramstr if c in PERMITTED_CHARS)
    return answer

#deformats the messages incoming from the server
def deformat(msg):
    var = strip(str(msg(2048).decode(format)))
    return var
#variable to make it easier to find server message.

#sends a message to the server.
def send(msg):
    message = msg.encode(format)
    message += b' ' * (header - len(message))
    serv.send(message)

#sequence to help a user login to the server.

def login():
    global loggedIn
    global session
    global secnum
    global servmsg
    attemptcounter = 0
    if attemptcounter == 3:
        print('You have exceeded the amount of allowed attempts. Please wait 5 minutes before')
    while attemptcounter < 4:
        print('Please enter your username')
        username = input('')
        send(f"3 {username}")
        sleep(1)
        servmsg = serv.recv(2048)
        print(f"[recieved] {servmsg}.")
        servmsg = strip(str(servmsg))
        if servmsg == 'False':
            print(f"[SERVER]: \tUsername, '{username}' does not exist. Please try again. Attempt {str(attemptcounter)}/3")
            attemptcounter = attemptcounter + 1
            continue
        elif servmsg == 'True':
            print(f"Username Exists.\n\nPlease enter your password.")
            break
        password = input('')
        password = hasher(password)
        pwdattempts = pwdattempts + 1
        send(f"1 {username} {password}")
        sleep(1)
        servmsg = serv.recv(2048)
        servmsg = strip(str(servmsg))
        if deformat(servmsg) == 'good':
            print("Login accepted, generating sessionID")
            servmsg = str(servmsg)
            servmsg.split()
            session = servmsg
            print("Testing session ID...")
        #the server will return 'good' and the session if it is good
        #the server will return 'bad' and nothing else if the login information was invalid.
        send(f"7 {session} {username}")
        sleep(1)
        servmsg = strip(serv.recv(2048))
        if servmsg == 'Good':
            print("Successfully logged in.")
            loggedIn = True
            return True
        elif servmsg == 'Bad':
            print('Failed to complete login sequence, resetting.')
            loggedIn = False
            return False
        else:
            print(f"Server message uninterpreted, expected 'Good', or 'Bad', Received [{str(servmsg)}")

#function that retains information from the client user regarding
#the account, and then sends the queries provided in server protocol
def createAccount():
    username = input("Please pick a unique username that you would like to link to your account.")
    send(f"3 {username}")
    if servmsg == 'False':
        password = input('Please pick a password for us to give you.')
        password = hasher(password)
        secnum = input("Would you like to create your own 9-digit security number? If so, type it now, if not we'll generate one for you.")
        while True:
            try:
                int(secnum)
            except Exception as e:
                print('Incorrect Format.')
            if secnum == '':
                print('Ok, generating secnum with account creation.')
                secnum = 1
                break
            elif not e:
                if len(int(secnum)) == 9:
                    print('Okay, your secnum is ' + str(secnum) + '.')
                    break
            elif e:
                continue
            send(f"2 {username} {password} {secnum}")
            if servmsg == 'True':
                break
            else:
                print(f"Failed, server returned {str(servmsg)}")

def balance(session, secnum):
    global servmsg
    send(f"4 {session} {secnum}")
    balance = servmsg
    print("[Server]: \tYour balance is " + str(balance) + ".")



def deposit():
    global loggedIn
    global session
    while loggedIn:
        print("Hello, " + loggedIn[0] + ".\nHow much would you like to deposit? If you'd like to view your balance, type 'bal'.")
        depositAmount = input('')
        if depositAmount.lower() == 'bal':
            balance()
            continue
        elif int(depositAmount):
            print("Okay, depositing the amount.")
            #in protocol, 4 is to deposit, and we're going to send the session, then the amount. The secnum is not required as this could not really be malicious act. :)
            send(f"4 {session} {str(depositAmount)}")
            sys.wait(2)
            servmsg = serv.recv(2048)
            #makes the message readable.
            servmsg = deformat(servmsg)
            #displays the message to the user.
            print(f"[Server]: '{servmsg}'. ")
            return None
        #if the user did not enter an integer.
        else:
            print(f"[Client] Invalid Format, sending you to the menu.\n")
            return None
#end of function

def withdrawal():
    global session
    global secnum
    global loggedIn
    if loggedIn:
        while True:
            bal = balance(session, secnum)
            print("Please enter the amount that you would like to withdrawal from your account. You have $" + str(bal) + " in your account.")
            withdrawalAmount = input('')
            print("Okay, we're attempting to withdrawal $" + str(withdrawalAmount) + " from your account.")
            send("5 " + str(session) + " " + str(secnum) + " " + str(withdrawalAmount))
            print("Sent server message.")
            servmsg = serv.recv(2048)
            servmsg = deformat(servmsg)
            print(f"[Server] : {servmsg}")


def init():
    while True:
        print('attempting to connect.')
        try:
            serv.connect(addr)
            print('connected')
            break
        except Exception as e:
            print(f"[{e}] , trying again.")
            continue
    print('Connected to: [' + str(addr) + '].')
    global loggedIn
    global session
    loggedIn = False
    started = False
    if not checkSession(): # this will check for a .txt file that will have a token that is the username that was last logged in with.
        while not loggedIn:
            print("\n\nWelcome to bankSystem!\nWould you like to:\n\tLogin(login)\n\tCreate an Account (create)\n\tHelp(help)")
            initInput = input('')
            initInput = initInput.lower()
            if initInput == 'login' or 'create' or 'help' and not started:
                started = True
                if initInput == 'login':
                    login()
                elif initInput == 'create':
                    createAccount()
                elif initInput == 'help':
                    help()
            else:
                print("Wrong input, please try again with the queries: 'login', 'create', or 'help'.\n")
                continue
    elif checkSession():
        timesgone = 0
        while loggedIn:
            if timesgone == 0:
                inp = input('What would you like to do?')
            elif timesgone > 1:
                inp = input('What else would you like to do? (help for commands).')
            if inp == 'deposit':
                deposit()
                continue
            elif inp == 'withdrawal':
                withdrawal()
                continue
            elif inp == 'balance':
                bal()
                continue
            elif inp == 'help':
                help()
            elif inp == 'exit' or 'close' or 'disconnect' and checkSession():
                send("!DISCONNECT " + str(session))
                break
            else:
                continue

#begins the program
init()