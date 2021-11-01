import socket
import serversocket
import os
import sys
import time
import f

print("Connecting to server...")

#loop for attempting to connect to the server
while True:
    try: f.socketsetup('192.168.0.56', '613')
        print("Connected to server: ")
    except: Exception as e