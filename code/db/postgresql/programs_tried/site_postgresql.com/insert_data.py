import psycopg2

conn = psycopg2.connect(database='suppliers2', user='normal', password='1234', host='localhost', port='5432')
#print(conn)
cur = conn.cursor()
#Insert values
'''sql = 'INSERT INTO vendors(vendor_name) VALUES(%s)'
vendor_name='3M'
VALUES= ([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]) #this is the correct method of passing values
cur.executemany(sql, VALUES)'''
#VERIFICATION
cur.execute('SELECT vendor_name FROM vendors')
print(cur.rowcount)
rows = cur.fetchall()
print(rows)


cur.execute('SELECT * FROM vendors')
print(cur.rowcount)
rows1 = cur.fetchall()
print(rows1)

#DELETE ROWS
sql = 'DELETE FROM vendors WHERE vendor_id=%s'
vendor_id = ([('25',),('26',),('27',),('28',),('29',),('30',)]) #this is the correct method of passing values.
cur.executemany(sql, vendor_id)
print(cur.rowcount)
cur.execute('SELECT * FROM vendors')
rows = cur.fetchall()
print(rows)



conn.commit()
conn.close()