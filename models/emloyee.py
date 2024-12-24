import sqlite3

class Employee:
    def __init__(self,NUMEMP,NOM,prenom,email,password,tel,ville,adresse,salaire,FONCTION,datemb,NBMHV,NBTHV):
        self.NUMEMP = NUMEMP
        self.NOM = NOM
        self.prenom = prenom
        self.email = email
        self.password = password
        self.tel = tel
        self.ville = ville
        self.adresse = adresse
        self.salaire = salaire
        self.FONCTION = FONCTION
        self.datemb = datemb
        self.NBMHV = NBMHV
        self.NBTHV = NBTHV
    @classmethod
    def search_by_filters(cls, name, fonction, min_salary, max_salary, start_date, end_date):
        query = "SELECT * FROM employees WHERE 1=1"
        parameters = []

        if name:
            query += " AND (NOM LIKE ? OR prenom LIKE ?)"
            parameters.extend([f"%{name}%", f"%{name}%"])

        if fonction:
            query += " AND FONCTION = ?"
            parameters.append(fonction)

        if min_salary is not None:
            query += " AND salaire >= ?"
            parameters.append(min_salary)

        if max_salary is not None:
            query += " AND salaire <= ?"
            parameters.append(max_salary)

        if start_date:
            query += " AND datemb >= ?"
            parameters.append(start_date)

        if end_date:
            query += " AND datemb <= ?"
            parameters.append(end_date)

        # Execute the query using cursor methods
        conn = cls.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        conn.close()

        return results
    @staticmethod
    def search_employees(name=None, fonction=None):
        conn = Employee.get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM employees WHERE 1=1"
        params = []

        if name:
            query += " AND (NOM LIKE ? OR prenom LIKE ?)"
            name_param = f"%{name}%"
            params.extend([name_param, name_param])

        if fonction:
            query += " AND FONCTION LIKE ?"
            params.append(f"%{fonction}%")

        cursor.execute(query, params)
        employees = cursor.fetchall()
        conn.close()
        return employees if employees else []

    @staticmethod
    def get_db_connection():
        conn=sqlite3.connect("airplain.db")
        conn.row_factory=sqlite3.Row
        return conn    

    @staticmethod
    def get_all():
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees ")
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    @staticmethod
    def get_by_id(employee_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE NUMEMP = ?", (employee_id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None

    def create_employee(email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):
        conn=Employee.get_db_connection()
        db=conn.cursor()
        db.execute("""
        INSERT INTO employees (NOM, prenom, email, password, tel, ville, adresse, salaire, FONCTION, datemb)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (nom, prenom, email,password_hash, tel, ville, adresse, salaire, fonction, datemb))
        conn.commit()
        conn.close()

    def update_employee(crew_id,new_name,new_prenom,new_email,new_tel,new_ville,new_address,new_salaire,new_function):
        conn=Employee.get_db_connection()
        db=conn.cursor()
        if new_name:
            db.execute("UPDATE employees SET NOM= ? WHERE NUMEMP=?", (new_name,crew_id))
        if new_prenom:
            db.execute("UPDATE employees SET prenom= ? WHERE NUMEMP=?", (new_prenom,crew_id))
        if new_email:
            db.execute("UPDATE employees SET email= ? WHERE NUMEMP=?", (new_email,crew_id))
        if new_tel:
            db.execute("UPDATE employees SET tel= ? WHERE NUMEMP=?", (new_tel,crew_id))
        if new_ville:
            db.execute("UPDATE employees SET ville= ? WHERE NUMEMP=?", (new_ville,crew_id))
        if new_address:
            db.execute("UPDATE employees SET adresse= ? WHERE NUMEMP=?", (new_address,crew_id))
        if new_salaire:
            db.execute("UPDATE employees SET salaire= ? WHERE NUMEMP=?", (new_salaire,crew_id))
        if new_function:
            db.execute("UPDATE employees SET FONCTION= ? WHERE NUMEMP=?", (new_function,crew_id))                     
        conn.commit()
        conn.close()

    def delete_employee(emp_id):
        conn=Employee.get_db_connection()
        db=conn.cursor()
        db.execute("DELETE FROM employees WHERE NUMEMP=?", (emp_id,))
        conn.commit()    
        conn.close()
        
class FL_Employee(Employee):
    @staticmethod
    def get_employee_schedule(emp_id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        query = """
    SELECT 
        f.NUMVOL as flight_number,
        f.jvol as day,           
        f.HDEP as departure_time,
        f.durvol as duration,
        dep.NOM as departure,
        arr.NOM as arrival
    FROM flight f
    JOIN employee_vol ev ON ev.NUMVOL = f.id
    JOIN airport dep ON f.APORTDEP = dep.CODEV
    JOIN airport arr ON f.APORTARR = arr.CODEV
    WHERE ev.NUMEMP = ?
    ORDER BY f.jvol, f.HDEP
    """
        cursor.execute(query, (emp_id,))
        rows=cursor.fetchall()
        conn.close()
        if rows:
            return rows
        return None
    
    def get_NBMHV(self,id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NBMHV FROM employees WHERE NUMEMP=?",(id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    def get_NBTHV(self,id):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NBTHV FROM employees WHERE NUMEMP=?",(id,))
        row=cursor.fetchone()
        conn.close()
        if row:
            return row
        return None
    
    def set_NBMHV(self, employee_id, NBMHV):#set to O as default !!!!!
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET NBMHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))
        conn.commit()
        conn.close()

    def set_NBTHV(self, employee_id, NBMHV):
        conn=Employee.get_db_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE employees SET NBTHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))
        conn.commit()
        conn.close()

    