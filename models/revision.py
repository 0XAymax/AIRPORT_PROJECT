import sqlite3

class Revision():
    def __init__(self,NUMREV,RAPPORT,DATEREV,NBHREV,NUMAV,TECID):
        self.NUMREV = NUMREV
        self.RAPPORT = RAPPORT
        self.DATEREV = DATEREV
        self.NBHREV = NBHREV
        self.NUMAV = NUMAV
        self.TECID = TECID
    

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn 
    
    @staticmethod
    def get_all_revisions():
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision")
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_revision_by_id(id):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision WHERE NUMREV = ?", (id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    @staticmethod
    def get_revision_by_aircraft(numav):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision WHERE NUMAV = ?", (numav,))
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_revision_by_report(rapport):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision WHERE RAPPORT = ?", (rapport,))
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_revision_by_date(date):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision WHERE DATEREV = ?", (date,))
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_revision_by_tech(tecid):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM revision WHERE TECID = ?", (tecid,))
        rows = cur.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    def create_revision(report,daterev, nbhrev, aircraft_id,tec_id):
        conn = Revision.get_db_connection()
        cur = conn.cursor()
        cur.execute(""" INSERT INTO revision (RAPPORT,DATEREV,NBHREV,NUMAV,TECID)
        VALUES (?, ?, ?, ?, ?) """, (report,daterev, nbhrev, aircraft_id,tec_id))
        conn.commit()
        conn.close()
