import hashlib
import time
import sys
import socket, socketserver
import servermain
import serverf
import socketsetupprototype

#waits for client to connect, and then
#establishes a fluid socket connection
def socketsetup():
    s=socket.socket()
    host=socket.gethostname()
    port=12000 
    s.bind((host,port))
    s.listen(10)
    while True:
        c,addr=s.accept()
        print("Client connected" + addr)
        print('Got Connection from' + addr)
        content=c.recv(100).decode()
        if not content:
            break
        print(str(content))

def keyRequest(num):
    #make program request verification key from clientside
    input("hi")


def verify(verificationKey):
    #make program verify key that was sent from program
    input("hi")