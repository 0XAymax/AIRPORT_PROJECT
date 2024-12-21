import sqlite3
from models.aircraft import Aircraft
class Revision:
    def __init__(self, NUMREV, RAPPORT, DATEREV, NBHREV, avion, tec):
        self.NUMREV = NUMREV
        self.RAPPORT = RAPPORT
        self.DATEREV = DATEREV
        self.NBHREV = NBHREV
        self.avion = avion
        self.tec = tec
    @staticmethod
    def search_technician_revisions(tech_name=None, tech_id=None):
        conn = Aircraft.get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT r.*, e.NOM, e.prenom 
        FROM revision r
        JOIN employees e ON r.TECID = e.NUMEMP
        WHERE 1=1
        """
        params = []

        if tech_name:
            query += " AND (e.NOM LIKE ? OR e.prenom LIKE ?)"
            name_param = f"%{tech_name}%"
            params.extend([name_param, name_param])

        if tech_id:
            query += " AND e.NUMEMP = ?"
            params.append(tech_id)

        query += " ORDER BY r.DATEREV DESC"

        cursor.execute(query, params)
        revisions = cursor.fetchall()
        conn.close()
        return revisions if revisions else []

    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect("airplain.db")
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def get_all_revisions():
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM revision")
        rows = cursor.fetchall()
        conn.close()
        return rows  # Return raw rows

    @staticmethod
    def get_revision_by_id(numrev):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM revision WHERE NUMREV = ?", (numrev,))
        row = cursor.fetchone()
        conn.close()
        return row  # Return a single row

    @staticmethod
    def create_revision(rapport, daterev, numav, tecid):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO revision (RAPPORT, DATEREV, NBHREV, NUMAV, TECID) 
            VALUES (?, ?, ?, ?, ?)""",
            (rapport, daterev, 0, numav, tecid))  # Assuming NBHREV is initially set to 0
        conn.commit()
        conn.close()

    @staticmethod
    def update_revision(numrev, rapport=None, daterev=None):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        if rapport:
            cursor.execute("UPDATE revision SET RAPPORT = ? WHERE NUMREV = ?", (rapport, numrev))
        if daterev:
            cursor.execute("UPDATE revision SET DATEREV = ? WHERE NUMREV = ?", (daterev, numrev))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_revision(numrev):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM revision WHERE NUMREV = ?", (numrev,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_revisions_by_technician(tecid):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.*, 
                   e.NOM, 
                   e.prenom, 
                   e.NUMEMP 
            FROM revision r 
            LEFT JOIN employees e ON r.TECID = e.NUMEMP 
            WHERE r.TECID = ?
        """, (tecid,))
        rows = cursor.fetchall()
        conn.close()
        return rows  # Return rows with technician names

    @staticmethod
    def get_revisions_by_aircraft(numav):
        conn = Revision.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.*, 
                   e.NOM, 
                   e.prenom, 
                   e.NUMEMP 
            FROM revision r 
            LEFT JOIN employees e ON r.TECID = e.NUMEMP 
            WHERE r.NUMAV = ?
        """, (numav,))
        rows = cursor.fetchall()
        conn.close()
        return rows  # Return rows with technician names
