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
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
)

cur = conn.cursor()

#================================================
logfilename = ('testlog-' + '.txt')


def log(inp):
    print(inp)
    #creates a log file with the date, and time
    global logfilename 
    f = open(str(logfilename), "a")
    f.write("\n" + inp)
    f.close

def strip(param):
    paramstr = str(param)
    PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-" 
    answer = "".join(c for c in paramstr if c in PERMITTED_CHARS)
    return answer

def msgHandler(msg):
    print('[msghandler] recieved: ' + str(msg))
    if msg == 'hello':
        cur.execute("SELECT bal FROM bankSystem WHERE username='jw';")
        response = cur.fetchone()
        strip(response)
        print('reponse from sql ' + response)
        response = response.encode(format)
        responseLength = len(response)
        response += b' ' * (header - responseLength)
        conn.send(response)
        #logs for the user to see.    
        print('[server]: sent ' + str(response.decode(format)))
        return response
    

def handle_client(connection, address):
    log(f"[new connection]: " + str(address) + " has connected.")
    connected = True
    while True:
        if connected:
            msg = connection.recv(header).decode(format)
            print('recieved connection, and message. raw below.')
            print(str(msg))
            msg = msg.rstrip()
            print('stripped: ' + msg)
            log(f'[{str(address)}]: sent: "{msg}" | returned:"{str(h)}"')
            break
        else:
            continue
    connection.close()

def start():
    #queries user to log
    #listens for connections
    s.listen()
    log(f"Server is listening on '{str(server)}:{str(port)}'.")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        log(f"[connections] : {threading.active_count() - 1}")

start()