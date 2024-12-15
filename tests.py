import sqlite3
from datetime import datetime
con = sqlite3.connect("airplain.db")
cursor = con.cursor()
context={}
cursor.execute("SELECT e.NUMEMP,e.NUMVOL,v.APORTDEP,v.APORTARR,v.HDEP,v.durvol,v.jvol FROM employee_vol e,vol v WHERE e.NUMVOL=v.NUMVOL")
rows=cursor.fetchall()
print(rows)
con.commit()
con.close()
