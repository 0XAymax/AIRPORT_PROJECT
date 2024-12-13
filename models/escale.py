import sqlite3

class Escale:
    def __init__(self,IDESC,APORTESC,HARRESC,DURESC,NOORD,NUMVOL):
        self.IDESC=IDESC
        self.APORTESC=APORTESC
        self.HARRESC=HARRESC
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
        cursor.execute("SELECT * FROM escale ")
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
        row = cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_heure_arrive(idesc):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT HARRESC FROM escale WHERE IDESC = ?",(idesc,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row["HARRESC"]
        return None
    
    @staticmethod
    def get_escale_by_airport(APORTESC):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM escale WHERE APORTESC = ?",(APORTESC,))
        row = cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    def create_escale(airport_code, arrival_time, stop_duration, stop_order,flight_number):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO escale (APORTESC, HARRESC, DURESC, NOORD, NUMVOL) 
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
        row=cursor.fetchone()
        if row:
            return row
        return None
    
    def update_escale(idesc,aportesc,harresc,duresc,noord):
        conn=Escale.get_db_connection()
        cursor=conn.cursor()
        if aportesc:
            cursor.execute("UPDATE escale SET APORTESC = ? WHERE IDESC = ?", (aportesc,idesc))
        if harresc:
            cursor.execute("UPDATE escale SET HARRESC = ? WHERE IDESC = ?", (harresc,idesc))
        if duresc:
            cursor.execute("UPDATE escale SET DURESC = ? WHERE IDESC = ?", (duresc,idesc))
        if noord:
            cursor.execute("UPDATE escale SET NOORD = ? WHERE IDESC = ?", (noord, idesc))

        conn.commit()
        conn.close()    