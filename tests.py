import sqlite3
result ={}
conn=sqlite3.connect('airplain.db')
cursor=conn.cursor()
'''
cursor.execute("SELECT * FROM escale")
result= cursor.fetchall()
'''
query = """
  SELECT e.IDESC,a.NOM,e.HARMESC,e.DURESC,e.NOORD,e.NUMVOL FROM escale e,airport a WHERE e.APORTESC=a.CODEV
    """
cursor.execute(query)
result=cursor.fetchall()
conn.close()
print(result)


