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
        cursor.execute("SELECT v.NUMVOL,dep.NOM,arr.NOM ,HDEP,durvol,jvol FROM vol v INNER JOIN airport dep ON v.APORTDEP = dep.CODEV INNER JOIN  airport arr ON v.APORTARR = arr.CODEV WHERE NUMVOL = ?",(numvol,))
        row= cursor.fetchall()
        conn.close()
        if row:
            return row
        return None

    @staticmethod
    def get_depart_arrive(numvol):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT APORTDEP,APORTARR FROM vol WHERE NUMVOL =?",(numvol,))
        row=cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_vol_by_depart(depart):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(" SELECT v.* FROM vol v INNER JOIN airport a ON v.APORTDEP = a.CODEV WHERE a.NOM = ?",(depart,))
        row=cursor.fetchall()
        conn.close()
        if row:
            return row   
        return None
    
    @staticmethod
    def get_all_vol():
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT v.NUMVOL,dep.NOM AS APORTDEP, arr.NOM AS APORTARR FROM vol v INNER JOIN airport dep ON v.APORTDEP = dep.CODEV INNER JOIN  airport arr ON v.APORTARR = arr.CODEV")
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
    
    def create_vol(departure_airport, arrival_airport, departure_time,
               flight_duration, day_of_week): 
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day_of_week not in valid_days:
            raise ValueError(f"Invalid day. Must be one of {valid_days}")
        
        cursor.execute("""
            INSERT INTO vol (APORTDEP, APORTARR, HDEP, durvol, jvol) 
            VALUES (?, ?, ?, ?, ?)
            """, (departure_airport, arrival_airport, departure_time,
                  flight_duration, day_of_week))
        conn.commit()
        conn.close()

    def delete_vol(nomvol):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vol WHERE NUMVOL=?",(nomvol,))
        conn.commit()
        conn.close()
    
    def update_vol(numvol,aportdep,aportarr,hdep,durvol,jvol):   
        conn =Vol.get_db_connection()
        cursor=conn.cursor()
        if aportdep:
            cursor.execute("UPDATE vol SET APORTDEP = ? WHERE NUMVOL = ?",(aportdep,numvol))
        if aportarr:
            cursor.execute("UPDATE vol SET APORTARR = ? WHERE NUMVOL = ?",(aportarr,numvol))
        if hdep:
            cursor.execute("UPDATE vol SET HDEP = ? WHERE NUMVOL =?",(hdep,numvol))
        if durvol:
            cursor.execute("UPDATE vol SET durvol =? WHERE NUMVOL =?",(durvol,numvol))
        if jvol:
            cursor.execute("UPDATE vol SET jvol = ? WHERE NUMVOL = ?",(jvol,numvol))
        conn.commit()
        conn.close() 

    @staticmethod
    def get_vol_by_hdep(hdep):
        conn=Vol.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM vol WHERE HDEP = ?",(hdep,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None                       
    