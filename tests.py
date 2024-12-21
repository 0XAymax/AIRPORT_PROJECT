import sqlite3

conn=sqlite3.connect('airplain.db')
cursor=conn.cursor()

cursor.execute("ALTER TABLE employees_temp RENAME TO employees")
conn.commit()
conn.close()