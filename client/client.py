import socket
import hashlib
import time
import sys

header = 2048
port = 3305
format = 'UTF-8'
serverip = socket.gethostbyname(socket.gethostbyname())
addr = (serverip, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loggedIn = False
session = ''

def hasher(inp):
    return(str(hashlib.sha256(str(inp)).encode(format)).hexdigest())

def send(msg):
    message = msg.encode(format)
    message += b' ' * header - len(message))
    client.send(message)

def help():
    print('[HELP] : List of commands:')
    print("IF YOU'RE LOGGED IN:")
    print('[deposit] : Will allow you to enter an amount to deposit into the account balance.')
    print('[withdrawal] : Will allows you to enter an amount to withdraw from the account balance.')
    print('[balance] : Will display the balance of the coordinated account')
    print("\n\nIF YOU'RE NOT LOGGED IN:")

def init():
    global loggedIn
    loggedIn = False
    started = False
    checkToken() # this will check for a .txt file that will have a token that is the username that was last logged in with.
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