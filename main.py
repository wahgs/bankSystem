import socket
import serversocket
import os
import sys
import time
import f

print("Connecting to server...")

#loop for attempting to connect to the server
while not connection:
    try: f.socketsetup('192.168.0.56', '613')
    except: Exception as e
    if not e:
        print("Connected to server.")
        connection = True
    elif e:
        print("exception caught in connection sequence: " + e )
    
if connection:
    inputUsername = input("Hello, what is your username")
    serverf.finduser(inputUsername)