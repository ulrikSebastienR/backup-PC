import psycopg2
conn = psycopg2.connect(database='testsr',user='sr',password='1234',host='localhost',port='5432')
print(conn)

cur = conn.cursor()
cur.execute("CALL add_new_parts(%s,%s);",(part_id, part_name))
