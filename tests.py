import sqlite3
from datetime import datetime
con = sqlite3.connect("airplain.db")
cursor = con.cursor()
context={}

cursor.execute("SELECT ev.NUMEMP,e.NOM,e.prenom,e.email,e.tel FROM employee_vol ev, employees e WHERE ev.NUMEMP=e.NUMEMP")
rows=cursor.fetchall()
print(rows)


