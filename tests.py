import sqlite3
result ={}
conn=sqlite3.connect('airplain.db')
cursor=conn.cursor()
airport="dubai"
'''
cursor.execute("SELECT * FROM escale")
result= cursor.fetchall()
'''
query = """
  SELECT e.IDESC AS IDESC,a.NOM AS APORTESC,e.HARMESC AS HARMESC,e.DURESC AS DURESC ,e.NOORD AS NOORD FROM escale e,airport a WHERE e.APORTESC=a.CODEV AND a.NOM LIKE ?
    """
cursor.execute(query, ('%' + airport + '%',))
result=cursor.fetchall()
conn.close()
print(result)


