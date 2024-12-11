import sqlite3

class Airport:
    def __init__(self,CODEV,NOM,Pays,VILLE):
        self.CODEV = CODEV
        self.NOM = NOM
        self.Pays = Pays
        self.VILLE = VILLE

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn    
    
    @staticmethod
    def get_airport_by_name(nom):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM airport WHERE NAME = ?",(nom,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return Airport(row["CODEV"],row["NOM"],row["Pays"],row["VILLE"])
        return None
    
    @staticmethod
    def get_airport_by_id(codev):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM airport WHERE CODEV =?",(codev,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return Airport(row["CODEV"],row["NOM"],row["Pays"],row["VILLE"])
        return None
    
    @staticmethod
    def get_all():
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM airport ")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_city(codev):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT VILLE FROM airport WHERE CODEV =?",(codev,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row["VILLE"]
        return None
        


    
