import socket
import hashlib
import time
import sys

header = 64
port = 3305
format = 'UTF-8'
disconnect_message = "!DISCONNECT " + username
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket,SOCK_STREAM)

session = ''
username = ''

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
    send("1 " + hashed(usr) + " " + hashed(pwd))
    sys.sleep(3)
    try:
        session  = int(client.recv(2048))
    except Exception as e:
    if e:
        print("Error in developing the session, please try again.")
        f = False 


def select():
print("Would you like to withdrawal, view balance, or deposit?")
while goahead:
    inp1 = input(':').lower()
    if inp1 == 'withdrawal' or 'w' or 'with':
        inp1 = 4
    elif inp1 == 'view balance' or 'vb' or 'bal':
        inp1 = 5
    elif inp1 == 'deposit' or 'd' or 'dep':
        inp1 = 6
        
    else:
        print("[Client] Invalid Syntax, please try again.")
        continue


def sqnc(inp):
    inp = int(inp)
    while True:
        secnumRequired = False
        if inp == 1:
            print("How much would you like to withdrawal?")
            secnumRequired = True
            inp1 = input('')
        elif inp == 2:
            break
        elif inp == 3:
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
        print("[Client]: Message Sent")
        if client.recv(2048).decode(format) == 'done':
            print('[SERVER] Success')
        elif client.recv(2048).decode(format) == 'erorr':
            print('[SERVER] error')
            print('[Client] Restarting process due to error, please check'
            'that your input(s) are correct.')
            select()


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
        elif loggedIn:
            sqnc()



start()