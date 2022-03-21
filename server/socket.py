import server.f
import socket
import threading

connected = bool
# waits for client to connect, and then
# establishes a fluid socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

header = 64
port = 3305
server =  socket.gethostbyname(socket.gethostname())
addr = (server,port)
format = 'utf-8'
disconnect_message = '!disconnect'
s.bind(addr)

#handles socket clients
def handle_client(conn,addr):
    print(f"[new connection]: {addr} has connected.")
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            declaration = conn.recv(msg_length).decode(format)
            msg = (msg_length)
            if msg == disconnect_message:
                connected = False
            server.f.msgHandler(msg)
    conn.close()

#starts the server
def start():
    s.listen()
    print(f"Server is listening on {server}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[connections] : {threading.activeCount() - 1}")
print("[starting] : server is starting")
start()

def send(inp):
    # this is the sequence for allowing other classes to send messages to the client.
    if connected:
        c, addr = s.accept()
        c.send(inp).encode('UTF-8')


