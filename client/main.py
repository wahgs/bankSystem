import socket
import hashlib
import time
import sys

header = 64
port = 3305
format = 'UTF-8'
disconnect_message = "!DISCONNECT"
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket,SOCK_STREAM)

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
    send(f"1 " + hashed(usr) + " " + hashed(pwd))
    sleep(3)
    if client.


def create():
    print('creation sqnc')





#login / create starter
logOrCreate = input("Would you like to login, or create an account?(l/c)")
while True:
    if logOrCreate == 'l':
        login()
    elif logOrCreate == 'c':
        create()
    else:
        print("[erorr] improper syntax, try again.")