#https://pythonspot.com/python-database-programming-sqlite-tutorial/
import sqlite3 as lite
import sys
import os

print(os.getcwd())

con = lite.connect("test.db") #create a connection object to the database
print(con) #SQLite database connection object

cur = con.cursor() #return a cursor object for the connection
print(cur)

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)") #Every sqlite command is executed by cur.execute
    cur.execute("INSERT INTO Users VALUES(1, 'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2, 'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3, 'Greg')") #SQL commands accepts string with single quotes ' ' only

   
