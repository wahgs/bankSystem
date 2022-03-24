import socket
import hashlib

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
    client.send(send(message))
    
def login():
    print('login sqnc')

def create():
    print('creation sqnc')





#login / create starter
logOrCreate = input("Would you like to login, or create an account?(l/c)")
if logOrCreate == 'l':
    login()
elif logOrCreate == 'c':
    create()
else:
    