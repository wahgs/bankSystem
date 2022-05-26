from lib2to3.pgen2 import token
import socket
import hashlib
import time
import sys

header = 2048
port = 3305
format = 'UTF-8'
serverip = socket.gethostbyname(socket.gethostbyname())
addr = (serverip, port)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loggedIn = False
session = ''

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

#strips a message of commas, etc. In order to avoid injection, sloppiness, etc.
def strip(param):
    paramstr = str(param)
    PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
    answer = "".join(c for c in paramstr if c in PERMITTED_CHARS)
    return answer

#variable to make it easier to find server message.
servmsg = strip(str(serv.recv(2048).decode(format)))

#sends a message to the server.
def send(msg):
    message = msg.encode(format)
    message += b' ' * header - len(message))
    serv.send(message)

#sequence to help a user login to the server.
def login():
    attemptcounter = 0
    if attemptcounter == 3:
        print('You have exceeded the amount of allowed attempts. Please wait 5 minutes before')
    while attemptcounter < 4:
        print('Please enter your username')
        username = input('')
        send(f"3 {username}")
        if servmsg == 'False':
            print(f"[SERVER]: Username, '{username}' does not exist. Please try again. Attempt {str(attemptcounter)}/3")
            attemptcounter = attemptcounter + 1
            continue
        elif servmsg == 'True':
            print(f"Alright, please enter your password.")
            break
        password = input('')
        password = hasher(password)
        
        



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
            init()
        else:
            print(f"Failed, server returned {str(servmsg)}")


def init():
    print('attempting to connect.')
    serv.connect(addr)
    print('Connected to: [' + str(addr) + '].')
    global loggedIn
    global token
    loggedIn = False
    started = False
    checkSession() # this will check for a .txt file that will have a token that is the username that was last logged in with.
    while not loggedIn:
        print("Welcome to bankSystem! /n/nWould you like to:\nLogin(login)\nCreate an Account (create)\nHelp(help)")
        initInput = input('')
        initInput = initInput.lower()
        #handles incorrect input through the while loop, not allowing incorrect queries to pass.
        if initInput != 'login' or 'create' or 'help':
            print("Wrong input, please try again with the queries: 'login', 'create', or 'help'.\n")
            continue
        #handles the correct inputs.
        elif initInput is 'login' or 'create' or 'help' and not started:
            started = True
            if initInput is 'login':
                login()
            elif initInput is 'create':
                createAccount()
            elif initInput is 'help':
                help()
    while loggedIn:
        inp = input('What would you like to do?')
        if inp == 'deposit':
            deposit()
        elif inp == 'withdrawal':
            withdrawal()
        elif inp == 'balance':
            bal()
        elif inp == 'help':
            help()
        elif inp == 'exit' or 'close' or 'disconnect' and token:
            send("!DISCONNECT " + str(token))
            break
        else:
            continue


init() 