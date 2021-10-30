import hashlib
import time
import sys
import socket, socketserver
import serverf
import serversocket
#server side for bankSystem developed by grizhe

#waits for client to connect, and begins server connection
serversocket.socketsetup()

#validates connection to clientside program
serversocket.verify

serversocket.clientinput()

