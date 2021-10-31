import hashlib
import time
import sys
import socket, socketserver
import serverf
import serversocket

# server side for bankSystem developed by grizhe

# waits for client to connect, and begins server connection
serversocket.socketsetup()


while serversocket.connection is True:
    serversocket.listen()

