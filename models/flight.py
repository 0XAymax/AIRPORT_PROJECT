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
        if numvol:
            cursor.execute("UPDATE flight SET NUMVOL = ? WHERE id = ?",(numvol,numv))
        if aportdep:
            cursor.execute("UPDATE flight SET APORTDEP = ? WHERE id = ?",(aportdep,numv))
        if aportarr:
            cursor.execute("UPDATE flight SET APORTARR = ? WHERE id = ?",(aportarr,numv))
        if hdep:
            cursor.execute("UPDATE flight SET HDEP = ? WHERE id =?",(hdep,numv))
        if durvol:
            cursor.execute("UPDATE flight SET durvol =? WHERE id =?",(durvol,numv))
        if jvol:
            cursor.execute("UPDATE flight SET jvol = ? WHERE id = ?",(jvol,numv))
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
    
    '''THIS IS JUST FOR DESIGN FEATURES '''
    @staticmethod
    def get_all_airport_code():
        conn=Vol.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT CODEV FROM airport")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_all_aircraft_ID():
     conn=Vol.get_db_connection()
     cursor=conn.cursor()
     try:
        # Query example for SQLAlchemy
        results = cursor.execute("SELECT NUMAV FROM aircraft").fetchall()

        # Convert the results into a simple list
        aircraft_ids = [result[0] for result in results]  # Extract the ID from each tuple

        if not aircraft_ids:
            raise ValueError("No aircraft available")
        return aircraft_ids

     except Exception as e:
        print(f"Error fetching aircraft IDs: {e}")
        return []
