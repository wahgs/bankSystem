import socket
import time
import mariadb

connected = bool
# waits for client to connect, and then
# establishes a fluid socket connection
s = socket.socket()


# socketsetup function
host = socket.gethostname()
port = 3309
s.bind((host, port))
s.listen(10)
while True:
    c, addr = s.accept()
    print("Client connected" + addr)
    print('Got Connection from' + addr)
    content = c.recv(100).decode('UTF-8')
    if not content:
        break
    connected = True
    continue


def listen():
    while True:
        time.sleep(5)
        try:
            c, addr = s.accept()
        except Exception as e:
            print("No response from client yet, waiting...")

def send(inp):
    # this is the sequence for allowing other classes to send messages to the client.
    if connected:
        c, addr = s.accept()
        c.send(inp).encode('UTF-8')
