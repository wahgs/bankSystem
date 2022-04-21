import socket
import hashlib
import time
import sys

username = ''
header = 64
port = 3305
format = 'UTF-8'
disconnect_message = "!DISCONNECT " + username
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

loggedIn = False
session = ''

def hasher(inp):
    return str(hashlib.sha256(str(inp).encode('utf-8')).hexdigest())

def send(msg):
    message = msg.encode(format)
    msg_length = len(msg)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(str(message))
    
    
def login():
    print('please insert your username')
    usr = input(':')
    print('please insert your password')
    pwd = input(':')
    print('\n[LOGIN] Logging you in... please allow up to 5 seconds.')
    end("1 " + hasher(usr) + " " + hasher(pwd))
    if client.recv(2048).decode(format) == 'good':
        print()

def questions(inp):
    inp = int(inp)
    while True:
        secnumRequired = False
        if inp == 4:
            print("How much would you like to withdrawal?")
            secnumRequired = True
            inp1 = input('')
        elif inp == 5:
            break
        elif inp == 6:
            print("How much would you like to deposit?")
            secnumRequired = True
            inp1 = input('')
        if secnumRequired:
            print("Please insert your secnum")
            secnum = input('')
            message = inp + inp1 + session + secnum
        else:
            message = inp + inp1
        send(message)
        print("[Client]: Message sent to server")
        servermsg = client.recv(2048).decode(format)
        print(f"[Server]: {servermsg}")


def select():
    while True:
        print("Would you like to withdrawal, view balance, or deposit?")
        inp1 = input(':').lower()
        if inp1 == 'withdrawal' or 'w' or 'with':
            questions(3)
        elif inp1 == 'view balance' or 'vb' or 'bal' or 'balance':
            questions(5)
        elif inp1 == 'deposit' or 'd' or 'dep':
            questions(6)
        else:
            print("\n[Client] Invalid Syntax, please try again.")
            continue


p = True
b = True
def create():
    while b:
        print("Please state the username that you would like to use")
        username = input('')
        print('[Client] --> [Server] : Checking username availability, please hold')
        send('3 ' + hasher(username))
        while True:
            if client.recv(2048).decode(format) == 'good':
                userCheck = 'good'
                usr = True
                break
            elif client.recv(2048).decode(format) == 'ngod':
                print("[SERVER] : Username taken, please choose a different username")
                sys.sleep(2)
                b = True
            else:
                continue
    while p:
        print(f"Awesome, {username}, let's  get you setup with a password.")
        while True:
            print("\n Please create a password.")
            inpP = input('')
            print(f"Please type your password again, {username}")
            inpP2 = input('')
            if inpP == inpP2:
                pwd = True
                break
            else:
                print('Error, passwords did not match, please try again.')
                continue
    if usr and pwd:
        print("Account created, " + username.title() + ', ' + password(1) + '*'*(len(password)-1))
        server.send('2 ' + username + ' ' + password)



#login / create starter
def start():
    if not loggedIn:
        logOrCreate = input("Would you like to login, or create an account?(l/c)")
        while f:
            if logOrCreate.lower() == 'l':
                login()
                break
            elif logOrCreate.lower() == 'c':
                create()
                logOrCreate = 'l'
                continue   
    elif loggedIn:
        questions()


start()