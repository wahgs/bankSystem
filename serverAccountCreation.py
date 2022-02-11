import serverf.py
import servermain.py
import serversocket.py
import gzip
import time
import sys



accounts = {}

def create(username,password,email):
    while True:
        if accounts.usernames >= 3:
            purge()
        check = True
        for usrname in accounts.usernames:
            if usrname is username:
                socket.send(print("Username already in use, please try again."))
                check = False
                break
            else:
                continue  
        for emailServer in accounts.emails:
            if emailServer is email:
                check = False
                socket.send(print("Email is already in use, please try another email,  or try 'forgot password'."))
                break
            else:
                continue
        if check:
            accounts.append(username,password,email)
            return True

def purge():
    content = accounts
    with gzip.open(#INSERT FILE NAME 
    'FILE', 'wb') as f:
        f.write(content)
    accounts.clear()