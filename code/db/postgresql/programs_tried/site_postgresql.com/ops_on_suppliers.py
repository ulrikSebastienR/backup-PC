#https://www.postgresqltutorial.com/postgresql-python/create-tables/

import psycopg2

conn = psycopg2.connect(database="suppliers2",host="localhost",user="normal",password="1234")
print(conn)

#create tables https://www.postgresqltutorial.com/postgresql-python/create-tables/
commands = (
    """
    CREATE TABLE vendors (
    vendor_id SERIAL PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL
    )
        """,
        """
        CREATE TABLE parts (
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE part_drawings (
            part_id INTEGER PRIMARY KEY,
            file_extension VARCHAR(5) NOT NULL,
            drawing_data BYTEA NOT NULL,
            FOREIGN KEY (part_id)
            REFERENCES parts (part_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
            vendor_id INTEGER NOT NULL,
            part_id INTEGER NOT NULL,
            PRIMARY KEY (vendor_id, part_id),
            FOREIGN KEY (vendor_id) 
                REFERENCES vendors (vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE            
        )
        """
   ) 
    
    
update_table = ''' UPDATE vendors
          SET vendor_name = %s
          where vendor_id = %s
                    '''
vendor_id = 1
vendor_name = "3M Corp"
updated_rows = 0    

with conn:
    cur = conn.cursor()
       
    '''for command in commands:
        cur.execute(command)'''

    cur.execute(update_table, (vendor_id, vendor_name))
    updated_rows = cur.rowcount
    print("Now rows in table Vendor are", updated_rows)
    




# Query rows from the table https://www.postgresqltutorial.com/postgresql-python/query/
    #cur.execute(SELECT )