import socket
import time

header = 2048
port = 3305
format = "utf-8"
disconnect_message = "!DISCONNECT"
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    print(msg)
    message = msg.encode(format)
    print('encoded: ' + str(message))
    message += b' ' + (header - len(message))
    print('sending: ' + str(message))
    client.send(message)
    while True:
        servermsg = client.recv(2048).decode(format)
        if servermsg:
            print("[Server] : " + servermsg + ".'")
        elif servermsg == 'error':
            print("[ERROR] invalid syntax, please refer to the protocol sheet. idiot.")
        else:
            print('no apparent server response.')


inp = input("What is the message that you would like to send?")
send(inp)