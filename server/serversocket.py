import socket
import threading
import serverf
import sys

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


#handles socket clients
def handle_client(connection, address):
    print(f"[new connection]: " + str(address) + " has connected.")
    connected = True
    while connected:
        msg_length = connection.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            declaration = connection.recv(msg_length).decode(format)
            msg = (declaration)
            connection.send(serverf.msgHandler(msg).encode(format))

    connection.close()


#starts the server
def start():
    s.listen()
    serverf.log(f"Server is listening on '{str(server)}:{str(port)}'.")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        serverf.log(f"[connections] : {threading.activeCount() - 1}")
        

while True:
    logQ = input("Would you like the server to log to a file?")
    if logQ.lower() == 'yes' or 'y':
        print("Okay, the server will log to: [log.txt] in: /bankSystem/ ")
        serverf.logenable()
        serverf.log('Logging enabled.')
    elif logQ.lower() == 'no' or 'n':
        print("Okay, continuing.")
        break
    else:
        print("Improper syntax, try again with 'yes', 'y', 'no' or 'n'")


start()