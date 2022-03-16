from server import serversocket
import mariadb
# server side for bankSystem developed by grizhe

# waits for client to connect, and begins server connection
serversocket.socketsetup()


while serversocket.connection is True:
    serversocket.listen()


