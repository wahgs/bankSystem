import hashlib
import time
import sys
import socket, socketserver
import serverf
import serversocket
#server side for bankSystem developed by grizhe

#begins server connection
serversocket.socketsetup

#validates connection to clientside program

serversocket.verify

inp1 = input("firstinp")
inp2 = input("secondinp")

serverf.clientinput(inp1, inp2)