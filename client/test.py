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

inp = input("What is the message that you would like to send?")
send(inp)
print(f"Sent message, : {inp}.")
servermsg = client.recv(2048).decode(format)
if servermsg is str:
    print(f"[SERVER] :  {str(servermsg)}")
else:
    print("Server did not send a message back please restart the program to send another message")