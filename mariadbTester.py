import mariadb
from time import sleep

print("This function is designed to ensure that the mariaDB connection is stable, before deploying the webapp.")
conn = None
connected = False
user = 'root'
password = 'a'
host = 'localhost'
port = 3306
database = 'accounts'

def statement(arg):
    print(f"What would you like to change the {str(arg)} to?")

def mariaCheck():
    global conn, connected, user, password, host, port, database
    #var turns false when the connection credentials are true
    var = True
    while var:
        try:
            conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            connected = True
            var = False
            cur = conn.cursor()
        except Exception as e:
            print("MariaDB connection not default. Server error message below\n" + e)
        print("Attmpted Credentials below.")
        print(f"user='{user}', password='{password}', host='localhost', port='3306', database='accounts'")
        happened = False
        while not connected:
            if not happened:
                print("What would you like to change?")
            elif happened:
                print("What else would you like to change?")
            print('[username/password/host/pot/database/exit]')
            happened = True
            inp = input('')
            if inp.lower() == 'username':
                statement(inp.title())
                username = input('')
                continue
            elif inp.lower() == 'password':
                statement(inp.title())
                password = input('')
                continue
            elif inp.lower() == 'host':
                statement(inp.title())
                host = input('')
                continue
            elif inp.lower() == 'port':
                statement(inp.title())
                port = input('')
                continue
            elif inp.lower() == 'database':
                statement(inp.title())
                database=input('')
                continue
            elif inp.lower() == 'exit' or 'try again':
                break
    if not var:
        print("Do you give this program permission to reformat the mariaDB instance that you have connected it to?\nThis means that all of the data currently stored on said instance will be permanently deleted.")
        inp = input("[y/n]: ")
        if inp.lower() == 'y':
            while True:
                
                print('wip')
        elif inp.lower() == 'n':
            print("Okay, quitting program. Please prepare your database so it can be foramtted accordingly before proceeding.")
            sleep(5)
            quit()
        
