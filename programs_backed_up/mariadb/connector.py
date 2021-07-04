mport pymysql
import os

conn = pymysql.connect(user='nefaisrein',password='1234',host='localhost',database='test')
print(conn)

cur = conn.cursor()
print(cur)

cur.execute('select * from books;')
print(cur.rowcount)

print(cur.fetchall())

