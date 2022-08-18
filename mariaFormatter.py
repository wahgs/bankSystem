#This program will set up a mariadb instanace to be used with the following program.
import mariadb
#connects the computer to the mariadb database
user="root"
password="a"
host="localhost"
port=3306
database='accounts'
conn = mariadb.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database
)

cur = conn.cursor()

#Function used to create the database
def mariaFormat():
    #checks to see if there is any informationpresent in the database.
    cur.execute("SHOW TABLES;")
    data = cur.fetchall()
    #this means that there is no tables in the database, therefore there is no data. The program is to now format the database as the main program requires.
    if data != 'None':
        cur.execute("CREATE TABLE")