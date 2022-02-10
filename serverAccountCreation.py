import serverf.py
import servermain.py
import serversocket.py
import gzip
import time
import sys



accounts = {}

def create(username,password,email):
    if accounts.usernames >= 3:
        purge
    accounts.append(username,password,email)

def purge():
    content = accounts
    with gzip.open(#INSERT FILE NAME 
    'FILE', 'wb') as f:
        f.write(content)
    if