import sqlite3

class Crew():
    def __init__(self,NUMEMP,NUMVOL):
        self.NUMEMP = NUMEMP
        self.NUMVOL = NUMVOL
    
    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn
        

    @staticmethod
    def get_all_crew():
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("SELECT e.NUMEMP,e.NUMVOL,v.APORTDEP,v.APORTARR,v.HDEP,v.durvol,v.jvol FROM employee_vol e,vol v WHERE e.NUMVOL=v.NUMVOL")
        rows = db.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_crew_by_id(crew_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("SELECT ev.NUMEMP,e.NOM,e.prenom,e.email,e.tel,e.FONCTION,e.datemb,e.NBMHV,e.NBTHV FROM employee_vol ev, employees e WHERE e.NUMEMP=?", (crew_id,))
        rows = db.fetchall()
        conn.close()
        if rows:
         return rows
        return None

    @staticmethod
    def create_crew(flight_id,crew_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("INSERT INTO employee_vol (NUMEMP,NUMVOL) VALUES (?, ?)", (crew_id,flight_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_crew(crew_id, new_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("UPDATE employee_vol SET NUMEMP= ? WHERE NUMEMP=?", (new_id,crew_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_crew(crew_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("DELETE FROM employee_vol WHERE NUMEMP=?", (crew_id,))
        conn.commit()    
        conn.close()
