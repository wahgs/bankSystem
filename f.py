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
    

def sendinfo(param):
    s.send(param.encode('utf-8'))

def disband(reason):
    print("Program shutdown via internal kill switch.")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()

def toomanyattempts(reason):
    print("Program shutting down due to too many attempts, reason:")
    if reason:
        print("Reason: " + str(reason))
    elif not reason:
        print("No reason provided by program")
    time.sleep(5)
    sys.exit()

def wip():
    print("This section of the code is known to be buggy and is a work in progress.")

