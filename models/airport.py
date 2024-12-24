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
        query = "SELECT * FROM airport WHERE NOM LIKE ?"
        cursor.execute(query,('%'+nom+'%',))
        row=cursor.fetchall()
        conn.close()
        if row:
            return row
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
        
    def create_airport(code, name, country, city):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO airport (CODEV, NOM, Pays, VILLE) VALUES ( ?,?,?,?)",(code,name,country,city))
        conn.commit()
        conn.close()

    def delete_airport(codev):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM airport WHERE CODEV = ?",(codev,))
        conn.commit()
        conn.close()
        
    def update_airport(codev,new_name,new_pays,new_city):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        if new_name:
            cursor.execute("UPDATE airport SET NOM =? WHERE CODEV =?",(new_name,codev))
        if new_pays:
            cursor.execute("UPDATE airport SET Pays =? WHERE CODEV =?",(new_pays,codev))
        if new_city:
            cursor.execute("UPDATE airport SET VILLE =? WHERE CODEV =?",(new_city,codev))

        conn.commit()
        conn.close()    
    
    @staticmethod
    def get_airport_by_city(city):
        conn=Airport.get_db_connection()
        cursor=conn.cursor()
        query="SELECT * FROM airport WHERE VILLE LIKE ?"
        cursor.execute(query,('%'+city+'%',))
        rows =cursor.fetchall()
        if rows:
            return rows
        return None