import socket
import string

username = ''
header = 2048
port = 3305
format = 'UTF-8'
disconnect_message = "!DISCONNECT " + username
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# -------------------------------------------------------


def send(msg):
    message = msg.encode(format)
    msg = b' ' * (header - len(msg))
    client.send(message)
    servermsg = client.recv(2048).decode(format)
    while True:
        if servermsg:
            print(f"[server]: '{servermsg.rstrip()}'.")
            break
        else:
            continue

inp = input("What message would you like to send to the server?\n[Message]:")
send(inp)