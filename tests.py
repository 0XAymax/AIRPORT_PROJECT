import sqlite3
from models.crew import Crew
result ={}
conn=sqlite3.connect('airplain.db')
cursor=conn.cursor()
id=16
airport="dubai"
'''
cursor.execute("SELECT * FROM escale")
result= cursor.fetchall()
'''
query = """
  SELECT e.NUMEMP, ev.NUMVOL, e.NOM, e.prenom, e.email, e.tel, e.FONCTION, e.datemb, e.NBMHV, e.NBTHV FROM employees e JOIN employee_vol ev ON e.NUMEMP = ev.NUMEMP WHERE e.NUMEMP=?
    """
#cursor.execute(query, (id,))
result['crew']=Crew.get_crew_by_id(16)
conn.close()
print(type(result['crew'][0][9]))


