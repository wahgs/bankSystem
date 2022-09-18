from flask import Flask, redirect, url_for, render_template, request
import sys
import mariadb
import hashlib
import random
from time import sleep


#default mariadb info----------------------------
user="root"
password="a"
host="localhost"
port=3306
database='accounts'

#this is referenced in mariaconnector, saves space.
def statement(var):
    print(f"Please type new {var} that you would like to change below.")

#this will be run before the website will go live
#refer to mariaConector.txt for instructions, and explaination. As comments would not describe the complexity.
def mariaConnector():
    global conn, connected, user, password, host, port, database
    #var turns false when the connection credentials are true
    var = True
    #statement is used 
    print("Do you already have a database in your mariadb instance that you would like to link to this program?")
    inp = input("[User: (y/n)] ")
    if inp == 'y':
        print('please define the proper name of the database that you would like to connect to in your provided mariadb instance.')
        database = input("[User:] ")
        print('Has the database that you defined above already been formatted by this program to be used with this program? [y/n] (if unsure type n)')
        databasequery = input("[User:] ")
        if databasequery == 'y':
            databasequery = True
        elif databasequery == 'n':
            databasequery = False
        while var:
            try:
                conn = mariadb.connect(
                    user=username,
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
            print(f"user='{user}', password='{password}', host={host}, port={str(port)}, database={database}")
            happened = False
            while not connected:
                print("What credentials would you like to change? Type 'try again', or 'ta' to retry the connection.")
                print('[username/password/host/pot/database/exit]')
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
                elif inp.lower() == 'database':
                    statement(inp)
                    database = input('')
                    continue
                elif inp.lower() == 'exit' or 'try again' or 'ta':
                    var = True
        #this happens if the server is actually connected.
        while not var:
            print("Do you give this program permission to edit the database that you declared above? This means that the program will have permission modify and manipulate the defined database in your mariadb instance.")
            inp = input("[y/n]: ")
            if inp.lower() == 'y':
                while True:
                    #this needs to append all of the required tables into a database called bankSys using cur.execute... 
                    cur.execute("")
            elif inp.lower == 'n':
                print('Okay, shutting down program, please start a mariadb instance that you would give modifying permissions to running before you start this program again.')
                sleep(5)
                sys.exit()
    elif inp.lower() == 'n':
        while True:
            print("Okay, would you like to use a current database? Or create one? [use/create]")
            DBQ = input("[User:] ")
            cur.execute("SHOW DATABASES")
            dblist = cur.fetchall()
            if DBQ == 'use':
                print("What is the name of the database that you would like to use? (CaSe sensitive)")
                print("Here is a list of the databases that you have in your server:\n" + dblist)
                dbname = input("\n[User:] ")
                cur.execute("SHOW DATABASES LIKE '" + dbname + "';")
                dbnamereturn = cur.fetchone()
                if dbnamereturn == "None":
                    print("This database does not exist, please try again.")
                    continue
                elif dbnamereturn != "None":
                    print(f"Alright, we'll use the database, '{dbname}'!" )
                    database = dbname
                    break
            elif DBQ == 'create':
                print("What is the name that you would like for the database to be? {press enter for defualt")
                dbname = input("[User:] ")
                print("Attempting to create database")
                if dbname == '':
                    dbname = 'bankSys'
                else:
                    cur.execute("CREATE DATABASE " + dbname)
                    cur.commit
                cur.execute("SHOW DATABASES")
                dblist = cur.fetchall()
                if dbname in dblist:
                    print("Success, the database was successfully created.")
                elif dbname not in dblist:
                    print("There was an error creating the database, please try again, or manually insert the database that you would like to use.")
cur = conn.cursor()
#end mariadb info---------------------------

#hashes provided string to sha256
def hasher(inp):
    return(str(hashlib.sha256(str(inp)).encode('UTF-8')).hexdigest())


def sessionCreator(username):
    counter = 0
    session = ''
    attempts = 1
    working = True
    while working:
        if counter < 9:
            num = random.randint(0, 9)
            session = session + str(num)
            counter = counter + 1
            continue
        if counter == 9:
            cur.execute("SELECT sessionID FROM sessions WHERE sessionID=" + session)
            seshchecker = cur.fetchone()
            seshchecker = str(seshchecker)
            print(f"seshchecker: {seshchecker}")
            if seshchecker != 'None':
                attempts = attempts + 1
                session = ''
                counter = 0
                continue
            elif seshchecker == 'None':
                sql = "INSERT INTO sessions (sessionID, username) VALUES (?, ?)"
                data = (session, username)
                cur.execute(sql, data)
                conn.commit()
                print(f"commited, {data}. It took {attempts} attempts.")
                break


#
def mariaContentChecker():
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
    bankCheck = cur.execute("SELECT sessions")
    if bankCheck.lower() == 'None':
        print("bankSystem table does not exist.. creating")
        cur.execute(
            "INSERT bankSystem"
            "VALUES('username', 'password', 'secnum', 'bal');"
        )



def startup():
    #startup sequence needs to check that the mariadb instance is running, and that the instance is 
    print("Program initiating, checking for mariadb instance on based information.")
      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login(returned):
    if request.method == "GET":
        return render_template("loginuser.html")
    if request.method == "POST":
        user = request.form['nm']
        cur.execute("SHOW username FROM accounts WHERE username='" + user + "';")
        usercheck = cur.fetchone()
        if usercheck != 'None':
            return redirect(url_for("loginp, usernm=user"))
        else:
            return render_template("loginuserwrongpassword.html")

@app.route("/loginp")
def loginp(usernm):
    if user == None:
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template("loginpasswd.html")
        elif request.method == "POST":
            passwd = request.form['pwd']
            passhashed = hasher(passwd)
            cur.execute("SHOW username FROM accounts WHERE password='" + passhashed + "';")
            returneduser = cur.fetchone()
            if returneduser == usernm:
                sessionCreator()
                return redirect(url_for("dash", session))
            elif returneduser != usernm:
                return render_template("")