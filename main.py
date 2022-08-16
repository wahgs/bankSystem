from flask import Flask, redirect, url_for, render_template, request
import sys
import mariadb
import hashlib


#default mariadb info----------------------------
user="root",
password="a",
host="localhost",
port=3306,
database='accounts'
conn = mariadb.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database
)
cur = conn.cursor()
#end mariadb info---------------------------

#hashes provided string to sha256
def hasher(inp):
    return(str(hashlib.sha256(str(inp)).encode('UTF-8')).hexdigest())

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

def datacheck():
    global conn
    #assigns information for the program to connect to the mariaDB docker instance
    mariaConnectionInfoCorrect = False
    try:
        cur.execute("SHOW TABLES;")
        print("")
        mariaConnectionInfoCorrect = True
    except Exception as e:
        print("Connection invalid with default credentials. Please follow the prompt to set up your mariadb instance")
        while mariaConnectionInfoCorrect == False:
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
                if mariaContentChecker() == True:
                    print('mariadb connection established.')
                    return True

            except Exception as e:
                print(f"Error trying to connect: [{str(e)}]")
                print(f"Please enter data again...")
                mariaConnectionInfoCorrect = False
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
            mariaContentChecker()
        except Exception as e:
                print(f"Error trying to connect: [{str(e)}]")
                print(f"Please enter data again...")
                datacheck()


def mariacheck():
    print()
    datacheck()


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
            cur.execute("SHOW username FROM accounts WHERE password='" + passhashed"';")
            returneduser = cur.fetchone()
            if returneduser == usernm:
                return 