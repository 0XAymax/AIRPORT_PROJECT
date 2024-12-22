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
        db.execute("""SELECT ev.NUMEMP AS NUMEMP,e.NOM AS name,e.prenom AS last_name,
        e.email AS email,f.NUMVOL AS flight_number,f.APORTDEP AS departure_airport,
        f.APORTARR AS arrival_airport,f.HDEP AS departure_time
        FROM 
        employee_vol ev
        JOIN 
        employees e ON ev.NUMEMP = e.NUMEMP
        JOIN 
        flight f ON ev.NUMVOL = f.id;
        """)
        rows = db.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_crew_by_id(crew_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("""SELECT e.NUMEMP, ev.NUMVOL, e.NOM, e.prenom, e.email, e.tel, e.FONCTION, e.datemb, e.NBMHV, e.NBTHV FROM employees e 
        JOIN employee_vol ev ON e.NUMEMP = ev.NUMEMP WHERE e.NUMEMP=?""",(crew_id,))
        rows = db.fetchall()
        conn.close()
        if rows:
         return rows
        return None

    @staticmethod
    def create_crew(email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("""
        INSERT INTO employees (NOM, prenom, email, password, tel, ville, adresse, salaire, FONCTION, datemb)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (nom, prenom, email,password_hash, tel, ville, adresse, salaire, fonction, datemb))
        conn.commit()
        conn.close()

    @staticmethod
    def update_crew(crew_id, new_id,new_name,new_prenom,new_email,new_password,new_tel,new_ville,new_address,new_salaire,new_function,new_datemb):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        if new_id:
         db.execute("UPDATE employee_vol SET NUMVOL= ? WHERE NUMEMP=?", (new_id,crew_id))
        if new_name:
            db.execute("UPDATE employees SET NOM= ? WHERE NUMEMP=?", (new_name,crew_id))
        if new_prenom:
            db.execute("UPDATE employees SET prenom= ? WHERE NUMEMP=?", (new_prenom,crew_id))
        if new_email:
            db.execute("UPDATE employees SET email= ? WHERE NUMEMP=?", (new_email,crew_id))
        if new_password:
            db.execute("UPDATE employees SET password= ? WHERE NUMEMP=?", (new_password,crew_id))
        if new_tel:
            db.execute("UPDATE employees SET tel= ? WHERE NUMEMP=?", (new_tel,crew_id))
        if new_ville:
            db.execute("UPDATE employees SET ville= ? WHERE NUMEMP=?", (new_ville,crew_id))
        if new_address:
            db.execute("UPDATE employees SET adresse= ? WHERE NUMEMP=?", (new_address,crew_id))
        if new_salaire:
            db.execute("UPDATE employees SET salaire= ? WHERE NUMEMP=?", (new_salaire,crew_id))
        if new_function:
            db.execute("UPDATE employees SET FONCTION= ? WHERE NUMEMP=?", (new_function,crew_id))
        if new_datemb:
            db.execute("UPDATE employees SET datemb= ? WHERE NUMEMP=?", (new_datemb,crew_id))                        
        conn.commit()
        conn.close()

    @staticmethod
    def delete_crew(crew_id):
        conn=Crew.get_db_connection()
        db=conn.cursor()
        db.execute("DELETE FROM employee_vol WHERE NUMEMP=?", (crew_id,))
        conn.commit()    
        conn.close()
    
    @staticmethod
    def insert_crew_member(email,flight_id):
        conn=Crew.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NUMEMP FROM employees WHERE email = ?",(email,))
        row=cursor.fetchone()
        cursor.execute("INSERT INTO employee_vol (NUMEMP,NUMVOL) VALUES (?,?) ",(row[0],flight_id))
        conn.commit()
        conn.close()
    
    def check_flight_exists(numvol):
       conn=Crew.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM flight WHERE id = ?", (numvol,))
       result = cursor.fetchone()
       conn.close()

       return result is not None
    
    @staticmethod
    def check_email_exists(email):
       conn=Crew.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM employees WHERE email = ?", (email,))
       result = cursor.fetchone()
       conn.close()

       return result is not None
    
    @staticmethod
    def get_all_flights():
        conn=Crew.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT id FROM flight")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
