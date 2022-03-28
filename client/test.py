from http import server


{import socket

header = 64
port = 3305
format = "utf-8"
disconnect_message = "!DISCONNECT"
serverip = socket.gethostbyname(socket.gethostname())
addr = (serverip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
sleep(2)
servermsg = server.recv(2048)
if servermsg is str:
    print(f"[SERVER] :  {addr.recv(2048)")
else:
    print("Server did not send a message back please restart the program to send another message")
