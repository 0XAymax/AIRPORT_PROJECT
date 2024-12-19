import sqlite3


con = sqlite3.connect("airplain.db")
cursor = con.cursor()

cursor.execute("DROP TABLE vol;")

con.commit()
con.close()
