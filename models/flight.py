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
    
    def get_crew_by_flight_id(numvol):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NUMEMP FROM employee_vol WHERE NUMVOL=? ",(numvol,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    def add_crew_member(self,NUMEMP,NUMVOL):
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO employee_vol(NUMEMP,NUMVOL) VALUES(?,?)""",(NUMEMP,NUMVOL))
        conn.commit()
        conn.close()

    def create_vol(departure_airport, arrival_airport, departure_time,
               flight_duration, day_of_week, aircraft_id=None): 
        conn = Vol.get_db_connection()
        cursor = conn.cursor()
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day_of_week not in valid_days:
            raise ValueError(f"Invalid day. Must be one of {valid_days}")
        
        if aircraft_id is not None:
            cursor.execute("""
            INSERT INTO vol (APORTDEP, APORTARR, HDEP, durvol, jvol, NUMVOL) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (departure_airport, arrival_airport, departure_time,
                  flight_duration, day_of_week, aircraft_id))
            conn.commit()
            conn.close()

        else:
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
        