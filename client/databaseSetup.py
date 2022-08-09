import mariadb
import sys
# sets up mariadb

cur = conn.cursor()

#
def init():
    #scanning sequence to determine if certain tables are there v.s. not
    print("Checking for table: 'sessions'.")
    sessionCheck = cur.execute("SELECT sessions")
    if sessionCheck.title() == 'None':
        print("No sessions, would you like to create a session manager?")
        inp = input('')
        if inp.lower == 'y' or 'yes':
            print('ok, creating sessions')
            cur.execute(
                "INSERT sessions"
                "VALUES('sessionID', 'Username');"
            )
        elif inp.lower == 'n' or 'no':
            print("Ok, moving on.")
    print("Checking for table: bankSystem")
    bankCheck = cu.execute("SELECT sessions")
    if bankCheck.lower() == 'None':
        print("bankSystem table does not exist.. creating")
        cur.execute(
            "INSERT bankSystem"
            "VALUES('username', 'password', 'secnum', 'bal');"
        )
        
def datacheck():
    global conn
    #assigns information for the program to connect to the mariaDB docker instance
    print("Welcome, if you modified the provided mariadb image or volume in any form, please type 'mod' otherwise, press enter.'")
    inp1 = input('')
    if inp1 == 'mod':
        while True:
            print("What is the username?")
            user = input('')
            print("What is the password")
            password = input('')
            print("What is the host IP? (address can be 'localhost' as well.")
            host = input('')
            print("What is the port?")
            port = int(input(''))
            print('What is the database name? (press enter for default, default is accounts)')
            database = input('')
            if database == '':
                database = 'accounts'
            print("Okay, attempting to connect...")
            try:
                conn = mariadb.connect(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                )
                print("Connected!")
                init()
            except Exception as e:
                print(f"Error trying to connect: [{str(e)}]")
                print(f"Please enter data again...")
                datacheck()
    else:
        try:
            conn = mariadb.connect(
                user="root",
                password="a",
                host="localhost",
                port=3306,
                database='accounts'
            )
            print("Connected!")
            init()
        except Exception as e:
                print(f"Error trying to connect: [{str(e)}]")
                print(f"Please enter data again...")
                datacheck()

print("Calling function 'dataCheck'...")
datacheck()