from audioop import add
import socket
import threading
import serverf

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
s.bind(ADDR)

#handles socket clients
def handle_client(connection,address):
    print(f"[new connection]: " + str(address) + " has connected.")
    attempts = 0
    connected = True
    while connected:
        msg_length = connection.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            declaration = connection.recv(msg_length).decode(format)
            msg = (declaration)
            serverf.msgHandler(msg)
    connection.close()


#starts the server
def start():
    s.listen()
    print(f"Server is listening on '{str(server)}:{str(port)}'.")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[connections] : {threading.activeCount() - 1}")
        break
    print("[starting] : server is starting")


def send(inp):
    # this is the sequence for allowing other classes to send messages to the client.
    message = inp.encode(format)
    message += '' * (cHeader -len(message))

start()