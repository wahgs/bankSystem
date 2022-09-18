#reconstructing mariaconnector function
import mariadb
import sys
from time import sleep

user = ''
password = ''
host = ''
port = 3306
database = ''

def statement(var):
    print(f"Please type new {var} that you would like to change below.") 

def mariaCheckr():
    global connected
    print("In order for this website to launch, there needs to be a mariaDB instance running that this program can connect to. Please define the following login credentials:")
    print("*REFER TO README FOR HELP*\nUsername, Password, Host, and Port.")
    user = input("[Username]: ")
    password = input("[Password]: ")
    host = input("[Host]: ")
    port = input("[Port]: ")
    print("Okay, attempting to connect to the server using the provided credentials.")
    #turns true when connection information is correct
    connected = False
    #turns true when the database is officially defined
    dbdefined = False
    #turns true when the database is ready to be formatted.
    formatReady = False
    #while loop runs until connected    
    while not connected:
        try:
            conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port
            )
            cur = conn.cursor()
            connected = True
        except Exception as e:
            print("Error connecting to server. Recieved error: " + str(e))
            print("Please redefine one of the credentials, as the provided credentials are incorrect.")
            print(f"Username: '{username}', Password: '{password}', Host: '{host}', Port: '{port}'.")
            while True:
                print("\nWhat would you like to change? (user, password, host, or port) or 'try again' when you think you've entered the correct credentials.")
                inp = input('')
                if inp.lower() == 'username':
                    statement(inp.title())
                    username = input('')
                    continue
                elif inp.lower() == 'password':
                    statement(inp)
                    password = input('')
                    continue
                elif inp.lower() == 'host':
                    statement(inp)
                    host = input('')
                    continue
                elif inp.lower() == 'port':
                    statement(inp)
                    port = input('')
                    continue
                elif inp.lower() == 'exit' or 'try again' or 'ta':
                    break
                else:
                    print("Incorrect input\n")
                    continue
            break
    while connected and not dbdefined and not formatReady:
        print("\nGreat, you're connected. Have you already created and had the program format a database for you? [y/n]")
        databQuery = input('')
        if databQuery == 'y':
            cur.execute("SHOW DATABASES;")
            dblist = cur.fetchall()
            print(dblist)
            while True:
                print("\nPlease define the name of the database.")
                dbinput = input('')
                if dbinput in dblist:
                    database = dbinput
                    print("\nAwesome, the server will now move onto the next step of deploying.\n.\n.")
                    try:
                        mariadb.connect(
                            user=user,
                            password=password,
                            host=host,
                            port=port,
                            database=database
                        )
                        cur = conn.cursor()
                        print("\nAwesome, the server will now move onto the next step of deploying.\n.\n.")
                        dbdefined = True
                    except Exception as e:
                        print('ln195, error when attempting to connect to the database, when the database name was in the fetched list.')
                        print("Server error message: " + e)
                        print("Please try another database name, or close the program.")
                        continue
                elif dbinput not in dblist:
                    print("\nThe database was not detected to be in the server. Here are the options in the database.")
                    print(dblist)
                    continue
        elif databQuery == 'n':
            while True:
                print("Alright, what would you like the name of the new database to be? Here's a list of the databases already in the mariaDB server.")
                print("NOTICE: by submitting a name, you are allowing this program to create and manipulate information within the provided database name.")
                cur.execute("SHOW DATABASES;")
                #retrieves a list of the databases
                dblist = cur.fetchall()
                print(dblist)
                dbname = input('\n')
                if dbname not in dblist:
                    print("Okay, attempting to create the database.")
                    cur.execute("CREATE DATABASE " + dbname)
                    conn.commit
                    print("attempting creating database")
                    cur.execute("SHOW DATABASES;")
                    dblist = cur.fetchall()
                    if dbname in dblist:
                        print('successfully created the database.')
                        formatReady = True
                    elif dbname not in dblist:
                        print('error, the new database is not in the newly created dblist... line 224')
                elif dbname in dblist:
                    print("Name " + str(dbname) + " already used, please try another name that is not in the list. Restarting...\n\n")
                    continue
    while connected and dbdefined and formatReady:
    #initiates when the database has been defined, the program has declared that the database is ready to format, and that all of the connection credentials are valid.
        conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        cur = conn.cursor()
        print("Formatting the database")
        cur.executemany(
            "CREATE TABLE accounts("
            "username VARCHAR(64),"
            "password VARCHAR(64),"
            "SECNUM INT(9),"
            "BAL INT(24))"
        )
        print(conn.commit())
        print("Checking establishment of 'accounts' table...")
        cur.execute("SHOW TABLE accounts;")
        returned = cur.fetchall()
        if len(returned) < 4:
            print("Error formatting program. Please refer to README *manually creating database* for instructions.")
            sleep(5)
            sys.exit()
        print("Successfully created the account's table. Creating Sessions table.")
        cur.executemany(
            "CREATE TABLE sessions("
            "sessionID INT(9),"
            "username VARCHAR(64) )"
        )
        print("Checking establishment of 'sessions' table...")
        cur.execute("SHOW TABLE sessions;")
        returned = cur.fetchall()
        if len(returned) == 2:
            print("Completely formatted the database. Please manually check the mariaDB instance with software like 'Navicat'.")
        else:
            print("Server check invalid, please manually check the mariaDB instance with software like navicat, to ensure that the instance meets the program standards.")
#end of automatic-mariadb-setup. could require manual setup >:(