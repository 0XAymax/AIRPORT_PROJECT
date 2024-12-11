import sqlite3

class Vol:
    def __init__(self,NUMVOL,APORTDEP,APORTARR,HDEP,durvol,jvol):
        self.NUMVOL=NUMVOL
        self.APORTDEP=APORTDEP
        self.APORTARR=APORTARR
        self.HDEP=HDEP
        self.durvol=durvol
        self.jvol=jvol

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn
        
    @staticmethod
    def get_vol(numvol):
        conn=Vol.get_db_connection()
        cursor =conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE NUMVOL = ?",(numvol,))
        row= cursor.fetchone()
        conn.close()
        if row:
            return Vol(row["NUMVOL"],row["APORTDEP"],row["APORTARR"],row["HDEP"],row["durvol"],row["jvol"])
        return None

    @staticmethod
    def get_depart_arrive(numvol):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT APORTDEP,APORTARR FROM vol WHERE NUMVOL =?",(numvol,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_vol_by_depart(depart):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE APORTDEP = ?",(depart,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return Vol(row["NUMVOL"],row["APORTDEP"],row["APORTARR"],row["HDEP"],row["durvol"],row["jvol"])   
        return None
    
    @staticmethod
    def get_all_vol(numvol):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE NUMVOL = ?",(numvol,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_all_vol_by_depart(depart):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE APORTDEP =? ",(depart,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def count_flights():
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM vol")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    @staticmethod
    def get_vol_by_day(day):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE jvol = ?", (day,))
        rows = cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
