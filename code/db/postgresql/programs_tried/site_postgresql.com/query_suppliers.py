import psycopg2

conn = psycopg2.connect(database='suppliers2',user='normal',password='1234',host='localhost',port=5432)
#print(conn)

cur = conn.cursor()
rows = cur.execute('SELECT vendor_id, vendor_name FROM vendors')
print("total number of parts", cur.rowcount)
print(rows)

conn.commit()
conn.close()
