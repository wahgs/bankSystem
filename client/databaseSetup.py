import mariadb
import sys

# sets up mariadb
conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
)

cur = conn.cursor()

#
def init():

    #scanning sequence to determine if certain tables are there v.s. not
    sessionCheck = cur.execute("SELECT sessions")
    if sessionCheck.title() == 'None':
        print("No sessions, would you like to create a session manager?")
        inp = input('')
        if inp.lower == 'y' or 'yes':
            print('ok, creating sessions')
            cur.execute("")