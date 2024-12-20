import sqlite3


con = sqlite3.connect("airplain.db")
cursor = con.cursor()
cursor.execute("SELECT e.NUMEMP, ev.NUMVOL, e.NOM, e.prenom, e.email, e.tel, e.FONCTION, e.datemb, e.NBMHV, e.NBTHV FROM employees e JOIN employee_vol ev ON e.NUMEMP = ev.NUMEMP WHERE e.NUMEMP=16")
rows=cursor.fetchall()
con.close()
print(rows)