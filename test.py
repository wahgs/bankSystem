import mariadb
import sys
from time import sleep

conn = mariadb.connect(
    user="root",
    password="a",
    host="localhost",
    port=3306,
    database='accounts'
)

cur = conn.cursor()


#this needs to be formatted to remove the databases, and create a new one. :|
def format():
    tablesRemoved = False
    while not tablesRemoved:
        print('retrieving tables.')
        cur.execute("SHOW TABLES;")
        tables = cur.fetchall()
        for table in tables:
            cur.execute("DROP TABLE IF EXISTS " + str(table) + ";")
            print(f"Dropped table {str(table).title()}.")
            sleep(1)
        print("Completed list, tables; checking to see if there are any remaining.")
        cur.execute("SHOW TABLES;")
        tables = cur.fetchall()
        if tables == 'None':
            print("Successfully removed all tables.")
            tablesRemoved = True
        elif tables != 'None':
            print(f"[Server]: '{str(tables)}'.  [Program]: Not all tables have been removed. Trying again.")
            tablesRemoved = False
    print("Beginning formation.")
    formatting = True
    while formatting:
        print("Inserting table")