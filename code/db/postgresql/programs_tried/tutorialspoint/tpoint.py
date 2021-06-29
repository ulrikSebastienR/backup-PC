#https://www.tutorialspoint.com/postgresql/postgresql_python.htm

import psycopg2
conn = psycopg2.connect(database="tutorialpoints1", user="normal", password="1234", host = "127.0.0.1", port = "5432")
print("opened database successfully", conn)

cur = conn.cursor()
create_table = """CREATE TABLE company_new(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL, 
    ADDRESS CHAR(50),
    SALARY REAL,
    EMPLOYEE CHAR(1))
"""
cur.execute(create_table)
print("We created a table")

conn.commit()
conn.close()
