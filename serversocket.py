import hashlib
import time
import sys
import socket, socketserver
import servermain
import serverf
import socketsetupprototype
import f

#waits for client to connect, and then
#establishes a fluid socket connection
s = socket.socket()
#socketsetup function
def socketsetup():
    host=socket.gethostname()
    port=12000 
    s.bind((host,port))
    s.listen(10)
    while True:
        c,addr=s.accept()
        f.verify(c)
        print("Client connected" + addr)
        print('Got Connection from' + addr)
        content=c.recv(100).decode('UTF-8')
        if not content:
            return 'nocontent'
            break
        return content

def listen():
    while True:
        time.sleep(5)
        e=None
        try:
            c,addr=s.accept()
        except Exception as e:
            print("No response from client yet, waiting...")
        continue