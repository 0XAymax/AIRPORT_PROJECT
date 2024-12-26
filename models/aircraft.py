import sqlite3

class Aircraft:
    def __init__(self,NUMAV,TYPE,DATEMS,NBHDDREV,STATUS):
       self.NUMAV=NUMAV
       self.TYPE=TYPE
       self.DATEMS=DATEMS
       self.NBHDDREV=NBHDDREV
       self.STATUS=STATUS
    
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect('airplain.db')
        conn.row_factory = sqlite3.Row
        return conn  
    
    @staticmethod
    def get_by_id(numav):
        conn = Aircraft.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM aircraft WHERE NUMAV = ?", (numav,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Aircraft(row["NUMAV"], row["TYPE"], row["datems"], row["NBHDDREV"], row["status"])
        return None
    
    @staticmethod
    def get_status(numav): 
        conn  = Aircraft.get_db_connection()
        cursor =conn.cursor()
        cursor.execute("SELECT status FROM aircraft WHERE NUMAV = ?",(numav,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        return None
    
    @staticmethod
    def get_by_name(name):
        conn = Aircraft.get_db_connection()
        cursor =conn.cursor()
        query="SELECT * FROM aircraft WHERE TYPE LIKE ?"
        cursor.execute(query,('%'+name+'%',))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_nbhddrev(numav):
        conn=Aircraft.get_db_connection()
        cursor =conn.cursor()
        cursor.execute("SELECT NBHDDREV FROM aircraft WHERE NUMAV = ?",(numav,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        return None
    
    @staticmethod
    def get_datems(numav):
        conn=Aircraft.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT datems FROM aircraft WHERE NUMAV = ?",(numav,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row[0]
        return None
    @staticmethod
    def get_all_aircrafts():
        conn=Aircraft.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT *FROM aircraft ")
        row=cursor.fetchall()
        conn.close()
        if row:
            return row
        return None
    
    def create_aircraft( aircraft_type, datems, nbhddrev, status):
        conn = Aircraft.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO aircraft (TYPE, datems, NBHDDREV, status)
            VALUES (?, ?, ?, ?)""",
            (aircraft_type, datems, nbhddrev, status))
        conn.commit()
        conn.close()
    
    def update_aircraft(numav, aircraft_type=None, datems=None, nbhddrev=None, status=None):
        conn = Aircraft.get_db_connection()
        cursor = conn.cursor()

        if aircraft_type:
            cursor.execute("UPDATE aircraft SET TYPE = ? WHERE NUMAV = ?", (aircraft_type, numav))
        
        if datems:
            cursor.execute("UPDATE aircraft SET datems = ? WHERE NUMAV = ?", (datems, numav))
        
        if nbhddrev:
            cursor.execute("UPDATE aircraft SET NBHDDREV = ? WHERE NUMAV = ?", (nbhddrev, numav))
        
        if status:
            cursor.execute("UPDATE aircraft SET status = ? WHERE NUMAV = ?", (status, numav))
        
        conn.commit()
        conn.close()

    
    def delete_aircraft(numav):
        conn = Aircraft.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM aircraft WHERE NUMAV = ?", (numav,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_by_status(name):
        conn = Aircraft.get_db_connection()
        cursor =conn.cursor()
        cursor.execute("SELECT * FROM aircraft WHERE status = ?",(name,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows    
