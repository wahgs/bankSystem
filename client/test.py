import socket
import time

header = 64
port = 3305
format = "utf-8"
disconnect_message = "!DISCONNECT"
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(format)
    msg_length = len(msg)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
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
print(f"Sent message, : {inp}.")
send(inp)