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
        verifiedChecks = 0
        for usrname in accounts.usernames:
            if usrname is username:
                return False
            else:
                verifiedChecks + 1
        for password

        if verifiedChecks = 3:
            accounts.append(username,password,email)

def purge():
    content = accounts
    with gzip.open(#INSERT FILE NAME 
    'FILE', 'wb') as f:
        f.write(content)
    accounts.clear()
