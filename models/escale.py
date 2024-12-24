import sqlite3

class Escale:
    def __init__(self,IDESC,APORTESC,HARMESC,DURESC,NOORD,NUMVOL):
        self.IDESC=IDESC
        self.APORTESC=APORTESC
        self.HARMESC=HARMESC
        self.DURESC=DURESC
        self.NOORD=NOORD
        self.NUMVOL=NUMVOL

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn
    
    @staticmethod
    def get_all_escale():
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("""SELECT e.IDESC AS IDESC,a.NOM AS APORTESC,e.HARMESC AS HARMESC,e.DURESC AS DURESC ,e.NOORD AS NOORD,
                       e.NUMVOL AS NUMVOL FROM escale e,airport a WHERE e.APORTESC=a.CODEV """)
        row = cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_escale_by_numvol(numvol):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM escale WHERE NUMVOL=?",(numvol,))
        row = cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_heure_arrive(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT HARMESC FROM escale WHERE IDESC = ?",(idesc,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row["HARMESC"]
        return None
    
    @staticmethod
    def get_escale_by_airport(APORTESC):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        query = """
  SELECT e.IDESC AS IDESC,a.NOM AS APORTESC,e.HARMESC AS HARMESC,e.DURESC AS DURESC ,e.NOORD AS NOORD FROM escale e,airport a WHERE e.APORTESC=a.CODEV AND a.NOM LIKE ?
    """
        cursor.execute(query,('%'+APORTESC+'%',))
        row = cursor.fetchall()
        conn.close()
        return row
    
    def create_escale(airport_code, arrival_time, stop_duration, stop_order,flight_number):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO escale (APORTESC, HARMESC, DURESC, NOORD, NUMVOL) 
        VALUES (?, ?, ?, ?, ?)
        """, (airport_code, arrival_time, stop_duration, stop_order, flight_number))
        conn.commit()
        conn.close()

    def delete_escale(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM escale WHERE IDESC = ?", (idesc,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_escale_by_id(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM escale WHERE IDESC =?",(idesc,))
        row=cursor.fetchall()
        if row:
            return row
        return None
    
    def update_escale(idesc,aportesc,harresc,duresc,noord):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        if aportesc:
            cursor.execute("UPDATE escale SET APORTESC = ? WHERE IDESC = ?", (aportesc,idesc))
        if harresc:
            cursor.execute("UPDATE escale SET HARMESC = ? WHERE IDESC = ?", (harresc,idesc))
        if duresc:
            cursor.execute("UPDATE escale SET DURESC = ? WHERE IDESC = ?", (duresc,idesc))
        if noord:
            cursor.execute("UPDATE escale SET NOORD = ? WHERE IDESC = ?", (noord, idesc))

        conn.commit()
        conn.close()   
         
    def check_airport_exists(codev):
       conn=Escale.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM airport WHERE CODEV = ?", (codev,))
       result = cursor.fetchone()
       conn.close()

       return result is not None    
    
    def check_flight_exists(numvol):
       conn=Escale.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM flight WHERE id = ?", (numvol,))
       result = cursor.fetchone()
       conn.close()

       return result is not None
    
    @staticmethod
    def get_all_airport_code():
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NOM FROM airport")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_all_flights():
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT id FROM flight")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_airport_code_by_name(name):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT CODEV FROM airport WHERE NOM = ?",(name,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        return None