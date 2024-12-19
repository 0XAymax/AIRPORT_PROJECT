import sqlite3


con = sqlite3.connect("airplain.db")
cursor = con.cursor()
depart="SIN"
cursor.execute("SELECT NUMVOL,APORTDEP,APORTARR,HDEP,durvol,jvol FROM flight WHERE APORTDEP =? ",(depart,))

row= cursor.fetchall()

con.commit()
con.close()
print(row)