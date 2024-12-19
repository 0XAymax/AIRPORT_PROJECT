import sqlite3

class Vol:
    def __init__(self,id,NUMVOL,APORTDEP,APORTARR,HDEP,durvol,jvol):
        self.id=id
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
    def get_vol(id):
        conn=Vol.get_db_connection()
        cursor =conn.cursor()
        cursor.execute("""
    SELECT v.NUMVOL, dep.NOM, arr.NOM, HDEP, durvol, jvol
    FROM flight v
    INNER JOIN airport dep ON v.APORTDEP = dep.CODEV
    INNER JOIN airport arr ON v.APORTARR = arr.CODEV
    WHERE id = ?;
""",(id,))
        row= cursor.fetchall()
        conn.close()
        if row:
            return row
        return None

    @staticmethod
    def get_depart_arrive(id):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT APORTDEP,APORTARR FROM flight WHERE id =?",(id,))
        row=cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_vol_by_depart(depart):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(" SELECT v.NUMVOL, v.APORTDEP, v.APORTARR, v.HDEP, v.durvol, v.jvol FROM flight v INNER JOIN airport a ON v.APORTDEP = a.CODEV WHERE a.NOM = ?",(depart,))
        row=cursor.fetchall()
        conn.close()
        if row:
            return row   
        return None
    
    @staticmethod
    def get_all_vol():
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT v.NUMVOL,dep.NOM AS APORTDEP, arr.NOM AS APORTARR FROM flight v INNER JOIN airport dep ON v.APORTDEP = dep.CODEV INNER JOIN  airport arr ON v.APORTARR = arr.CODEV")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_all_vol_by_depart(depart):
        conn=Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NUMVOL,APORTDEP,APORTARR,HDEP,durvol,jvol FROM flight WHERE APORTDEP =? ",(depart,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def count_flights():
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM flight")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    @staticmethod
    def get_vol_by_day(day):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flight WHERE jvol = ?", (day,))
        rows = cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    def create_vol(numv,departure_airport, arrival_airport, departure_time,flight_duration, day_of_week): 
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day_of_week not in valid_days:
            raise ValueError(f"Invalid day. Must be one of {valid_days}")
        
        cursor.execute("""
            INSERT INTO flight (NUMVOL,APORTDEP, APORTARR, HDEP, durvol, jvol) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (numv,departure_airport, arrival_airport, departure_time,
                  flight_duration, day_of_week))
        conn.commit()
        conn.close()

    def delete_vol(id):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM flight WHERE NUMVOL=?",(id,))
        conn.commit()
        conn.close()
    
    def update_vol(numv,numvol,aportdep,aportarr,hdep,durvol,jvol):   
        conn =Vol.get_db_connection()
        cursor=conn.cursor()
        if numv:
            cursor.execute("UPDATE flight SET NUMVOL = ? WHERE id = ?",(numvol))
        if aportdep:
            cursor.execute("UPDATE flight SET APORTDEP = ? WHERE id = ?",(aportdep,numvol))
        if aportarr:
            cursor.execute("UPDATE flight SET APORTARR = ? WHERE id = ?",(aportarr,numvol))
        if hdep:
            cursor.execute("UPDATE flight SET HDEP = ? WHERE id =?",(hdep,numvol))
        if durvol:
            cursor.execute("UPDATE flight SET durvol =? WHERE id =?",(durvol,numvol))
        if jvol:
            cursor.execute("UPDATE flight SET jvol = ? WHERE id = ?",(jvol,numvol))
        conn.commit()
        conn.close() 

    @staticmethod
    def get_vol_by_hdep(hdep):
        conn=Vol.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM flight WHERE HDEP = ?",(hdep,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None                       
    
    def check_airport_exists(codev):
       conn=Vol.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM airport WHERE CODEV = ?", (codev,))
       result = cursor.fetchone()
       conn.close()

       return result is not None
    
    def aircraft_is_available(numvol):
       conn=Vol.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT status FROM aircraft WHERE NUMAV =?",(numvol,))
       result=cursor.fetchone()

       if result:
           return result[0]
       return None
    
    def aircraft_exists(numav):
       conn=Vol.get_db_connection()
       cursor=conn.cursor()

       cursor.execute("SELECT 1 FROM aircraft WHERE NUMAV = ?", (numav,))
       result = cursor.fetchone()
       conn.close()

       return result is not None