this was all notes that are no longer necessary:

todo items left for the program before completion, and 'release' of 1.0




server ==============
- create more server prints, and figure out how to automatically timeout
    a session if it has not done anything, but there was no disconnect_message
    recieved from the client
-verify session with client ip
-double check all functions are properly written
- on main desktop, test every single function if possible, create a checklist,
    or list on todoist, and go through every single function
-serversocket.send() function needs to meet up to the client.recv(BYTES)
    byte amount -- similar to the function developed in the client side.

client ==============
-make sure that when the server sends 'error' it is properly recieved
-figure out how to declare disconnect_message, or make it so that the terminal
    / program is not actually closed out until the server responds saying 'ok'


