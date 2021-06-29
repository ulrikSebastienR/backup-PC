#https://www.postgresqltutorial.com/postgresql-python/connect/
#1 direct connection
import psycopg2

conn = psycopg2.connect(database="suppliers", host="localhost",user='normal',password='1234')
print(conn)

#2 Using file
from configparser import ConfigParser

def file_connect(filename, section):
    parser = ConfigParser()
    print(parser)
    x = parser.read(filename)
    print("x", x)

    db={}

    if parser.has_section(section):
        params = parser.items(filename)
        for param in params:
            db[param[0]] = param[1]

    else:
        print("section {} not found in file {}".format(section,filename))

    return db

file_connect('pw.ini','postgresql')



