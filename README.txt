this was all notes that are no longer necessary:

todo items left for the program before completion, and 'release' of 1.0

server - 
have server reply with 'invform' short for invalid-format, when the format is invalid.

test -
- if the server replies that the format is invalid, have the user redo their inputs.

from here, update client/client.py to reform to the code that is therefore set by the interactions between test.py, and server.py 

let's hope to spend less than one week before the version 1.0 can be 'released'

griz - 3/29 @ 1:00 am sharp

- error when connected to server using test.py - input was 'hello'

Exception in thread Thread-1 (handle_client):
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "c:\Users\grizhe\Desktop\bankSystem\server\serversocket.py", line 26, in handle_client
    msg_length = conn.recv(header).decode(format)
NameError: name 'conn' is not defined
c:\Users\grizhe\Desktop\bankSystem\server\serversocket.py:43: DeprecationWarning: activeCount() is deprecated, use active_count() instead
  print(f"[connections] : {threading.activeCount() - 1}")
[connections] : 0
[starting] : server is starting
PS C:\Users\grizhe\Desktop\bankSystem> 