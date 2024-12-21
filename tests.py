import sqlite3


context={}
con = sqlite3.connect("airplain.db")
cursor=con.cursor()
cursor.execute("SELECT v.id, a.TYPE, dep.NOM AS APORTDEP, arr.NOM AS APORTARR FROM flight v INNER JOIN airport dep ON v.APORTDEP = dep.CODEV INNER JOIN airport arr ON v.APORTARR = arr.CODEV INNER JOIN aircraft a ON v.NUMVOL = a.NUMAV")
rows=cursor.fetchall()
con.close()
