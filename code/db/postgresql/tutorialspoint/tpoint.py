#https://www.tutorialspoint.com/postgresql/postgresql_python.htm

import psycopg2
conn = psycopg2.connect(database="tutorialpoints1", user="normal", password="1234", host = "127.0.0.1", port = "5432")
print("opened database successfully", conn)

cur = conn.cursor()
'''create_table = """CREATE TABLE company_new(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL, 
    ADDRESS CHAR(50),
    SALARY REAL,
    EMPLOYEE CHAR(1))"""
    commented out create table as we dont need it anymore'''


'''cur.execute("""INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) 
 VALUES (3, 'Bostian', 23, 'US', 40000)""")
print("We inserted a record")'''

cur.execute("DELETE FROM company WHERE id=2")

print("No of rows are", cur.rowcount)

cur.execute("SELECT id, name, address, salary FROM COMPANY")
print("No of rows NOW are", cur.rowcount)
rows = cur.fetchall()
print(rows)

for row in rows:
    print("id is {} for employee with name {}, address {} and salary {}".format(row[0], row[1], row[2], row[3]))

conn.commit()
conn.close()
