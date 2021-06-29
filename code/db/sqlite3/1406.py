import sqlite3
conn = sqlite3.connect('1406.db')
cur = conn.cursor()
#print(cur)

"""sql_create_table_total_marks = '''create table total_marks(
    roll id integer PRIMARY KEY,
    name varchar(10),
    total_marks smallint
    );'''
cur.execute(sql_create_table_total_marks)

sql_insert_1 = ["insert into total_marks values(2, 'shyam', 420);", "insert into total_marks values(3, 'sr', 920);", "insert into total_marks values(4, 'singh', 630);"]
for i in sql_insert_1:
    cur.execute(i)

sql_select_1 = '''select * from total_marks;'''
cur.execute(sql_select_1)
print(cur.fetchall())

sql_select_2 = '''select * from total_marks where total_marks>450;'''
cur.execute(sql_select_2)
print(cur.fetchall())"""

print(f'row count for cursor is {cur.rowcount}')
conn.commit()
conn.close()
