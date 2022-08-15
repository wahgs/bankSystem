import mariadb

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

cur = conn.cursor()
    