import hashlib
import time
import sys
import socket, socketserver
import servermain
import serversocket
#functions "class'" for servermain.py developed by grizhe
def clientinput(firstInput, secondInput):
    try:
        if servermain.inp1 == firstInput | servermain.inp2 == secondInput:
            print("inputs correct")
        
    except Exception as e:
        print("error in servermain.clientinput")
    finally:
        return "continue"

def 