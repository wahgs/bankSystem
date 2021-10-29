import socket
import serversocket
import os
import sys
import time
import main
import hashlib

s=socket.socket()
def socketsetup(host, port):
    try: s.connect((host,port))
    except: Exception, print("Couldn't connect to host.")
    print("Connected to server: " + str(host))

def sendinfo(param):
    s.send(param.encode('utf-8'))
    