
import sqlite3
import os

# Get absolute path to the database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root directory of project
db_path = os.path.join(BASE_DIR, "instance", "airplain.db")

# -------------------------------------------------------------
# Base DAO class for handling SQLite database operations.
# -------------------------------------------------------------
class DAO:
    def __init__(self, db_path):
        """
        Initializes the DAO with the database path.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path

    def get_connection(self):
        """
        Returns a new SQLite connection.

        This method opens a new connection to the SQLite database each time it is called.
        It's important to use a fresh connection to avoid database lock issues.
        """
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=()):

        with self.get_connection() as con:
            cursor = con.cursor()  # Create a new cursor for the query
            cursor.execute(query, params)
            return cursor.fetchall()  # Fetch all results of the query

    def execute_non_query(self, query, params=()):

        with self.get_connection() as con:
            cursor = con.cursor()  # Create a new cursor for the query
            cursor.execute(query, params)
            con.commit()  # Commit the changes to the database


# -------------------------------------------------------------
# EmployeeDAO class for handling operations related to 'employees' table.
# -------------------------------------------------------------
class EmployeeDAO(DAO):
    def __init__(self, db_path):
        super().__init__(db_path)

    def get_by_id(self, employee_id):
        return self.execute_query("SELECT * FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_by_full_name(self, last_name, first_name):
        return self.execute_query("SELECT * FROM employees WHERE NOM = ? AND prenom = ?", (last_name, first_name))

    def get_by_email(self, email):
        return self.execute_query("SELECT * FROM employees WHERE email = ?", (email,))

    def get_by_city(self, city):
        return self.execute_query("SELECT * FROM employees WHERE ville = ?", (city,))

    def get_by_function(self, function):
        return self.execute_query("SELECT * FROM employees WHERE FONCTION = ?", (function,))

    def get_by_salary_range(self, min_salary, max_salary):
        return self.execute_query("SELECT * FROM employees WHERE salaire BETWEEN ? AND ?", (min_salary, max_salary))

    def get_full_name_by_id(self, employee_id):
        return self.execute_query("SELECT NOM, prenom FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_email_by_id(self, employee_id):
        return self.execute_query("SELECT email FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_password_hash_by_id(self, employee_id):
        return self.execute_query("SELECT password FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_phone_by_id(self, employee_id):
        return self.execute_query("SELECT tel FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_address_by_id(self, employee_id):
        return self.execute_query("SELECT adresse FROM employees WHERE NUMEMP = ?", (employee_id,))

    def get_salary_by_id(self, employee_id):
        return self.execute_query("SELECT salaire FROM employees WHERE NUMEMP = ?", (employee_id,))

    def set_full_name(self, employee_id, last_name, first_name):
        self.execute_query("UPDATE employees SET NOM = ?, prenom = ? WHERE NUMEMP = ?", (last_name, first_name, employee_id))

    def set_email(self, employee_id, email):
        self.execute_query("UPDATE employees SET email = ? WHERE NUMEMP = ?", (email, employee_id))

    def set_password_hash(self, employee_id, password_hash):
        self.execute_query("UPDATE employees SET password = ? WHERE NUMEMP = ?", (password_hash, employee_id))

    def set_phone(self, employee_id, phone):
        self.execute_query("UPDATE employees SET tel = ? WHERE NUMEMP = ?", (phone, employee_id))

    def set_address(self, employee_id, address):
        self.execute_query("UPDATE employees SET adresse = ? WHERE NUMEMP = ?", (address, employee_id))

    def set_salary(self, employee_id, salary):
        self.execute_query("UPDATE employees SET salaire = ? WHERE NUMEMP = ?", (salary, employee_id))

    def set_city(self, employee_id, city):
        self.execute_query("UPDATE employees SET ville = ? WHERE NUMEMP = ?", (city, employee_id))

    def set_function(self, employee_id, function):
        self.execute_query("UPDATE employees SET FONCTION = ? WHERE NUMEMP = ?", (function, employee_id))

    def create(self, email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):

        self.execute_non_query("""
        INSERT INTO employees (email, password, NOM, prenom, tel, ville, adresse, salaire, FONCTION, datemb)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb))
class FL_EmployeeDAO(EmployeeDAO):#class for employees that fly
    def __init__(self, db_path):
        super().__init__(db_path)
    def get_NBMHV(self,id):
        return self.execute_query("SELECT NBMHV FROM employees WHERE id=?",id)
    def get_NBTHV(self,id):
        return self.execute_query("SELECT NBTHV FROM employees WHERE id=?",id)
    def set_NBMHV(self, employee_id, NBMHV):
        self.execute_query("UPDATE employees SET NBMHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))
    def set_NBTHV(self, employee_id, NBMHV):
        self.execute_query("UPDATE employees SET NBTHV = ? WHERE NUMEMP = ?", (NBMHV, employee_id))

    def create(self, email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb):

        self.execute_non_query("""
        INSERT INTO employees (email, password, NOM, prenom, tel, ville, adresse, salaire, FONCTION, datemb)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (email, password_hash, nom, prenom, tel, ville, adresse, salaire, fonction, datemb))
        if self.get_by_email(email):
            self.set_NBMHV(self.get_by_email(email)[0][0],0)
            self.set_NBTHV(self.get_by_email(email)[0][0],0)
        else:
            raise ValueError(f"Employee with email {email} not found.")


class RevisionDAO(DAO):
    def __init__(self, db_path):
        super().__init__(db_path)  # Call the parent DAO's constructor

    def get_by_aircraft(self, aircraft_id):
        # Get revisions for a specific aircraft by its ID (NUMAV), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE NUMAV = ? ORDER BY NUMREV DESC", (aircraft_id,))

    def get_by_revision_id(self, revision_id):
        # Get a revision by its unique revision ID (NUMREV), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE NUMREV = ? ORDER BY NUMREV DESC", (revision_id,))

    def get_by_report(self, rapport):
        # Get revisions based on the report (RAPPPORT), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE RAPPPORT = ? ORDER BY NUMREV DESC", (rapport,))

    def get_by_date(self, date):
        # Get revisions based on the revision date (DATEREV), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE DATEREV = ? ORDER BY NUMREV DESC", (date,))

    def get_by_hours(self, hours):
        # Get revisions based on the number of hours (NBHREV), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE NBHREV = ? ORDER BY NUMREV DESC", (hours,))

    def get_by_technician(self, technician_id):
        # Get revisions based on the technician ID (TECID), ordered by NUMREV DESC
        return self.execute_query("SELECT * FROM revision WHERE TECID = ? ORDER BY NUMREV DESC", (technician_id,))
    def create_rev(self,report,daterev,aircraft_id,nbhrev,tec_id):
        self.execute_non_query("""
        INSERT INTO employees (RAPPORT,DATEREV,NBHREV,NUMAV,TECID)
        VALUES (?, ?, ?, ?, ?, ?) """, (report,daterev, nbhrev, aircraft_id,tec_id))# I found some logical errors in the db!!!!!

class AirportDAO(DAO):
    def __init__(self, db_path):

        super().__init__(db_path)  # Call the parent DAO's constructor

    def get_all(self):

        return self.execute_query("SELECT * FROM airport")

    def get_by_code(self, code):

        return self.execute_query("SELECT * FROM airport WHERE CODEV = ?", (code,))

    def get_by_name(self, name):

        return self.execute_query("SELECT * FROM airport WHERE NOM = ?", (name,))

    def get_by_country(self, country):

        return self.execute_query("SELECT * FROM airport WHERE Pays = ?", (country,))

    def get_by_city(self, city):

        return self.execute_query("SELECT * FROM airport WHERE VILLE = ?", (city,))
    def create(self, code, name, country, city):

        self.execute_non_query("""
        INSERT INTO airport (CODEV, NOM, Pays, VILLE) 
        VALUES (?, ?, ?, ?)
        """, (code, name, country, city))

    def delete(self, code):

        self.execute_non_query("DELETE FROM airport WHERE CODEV = ?", (code,))

class EscaleDAO(DAO):
    def __init__(self, db_path):

        super().__init__(db_path)  # Call the parent DAO's constructor

    def get_by_flight(self, flight_id):

        return self.execute_query("SELECT * FROM escale WHERE NUMVOL = ?", (flight_id,))

    def get_by_airport(self, airport_code):

        return self.execute_query("SELECT * FROM escale WHERE APORTESC = ?", (airport_code,))

    def get_by_arrival_time(self, harm_mesc):

        return self.execute_query("SELECT * FROM escale WHERE HARMESC = ?", (harm_mesc,))

    def get_by_duration(self, dur_esc):

        return self.execute_query("SELECT * FROM escale WHERE DURESC = ?", (dur_esc,))
    def create(self, airport_code, arrival_time, stop_duration, flight_number, stop_order):

        self.execute_non_query("""
        INSERT INTO escale (APORTESC, HARMESC, DURESC, NOORD, NUMVOL) 
        VALUES (?, ?, ?, ?, ?)
        """, (airport_code, arrival_time, stop_duration, stop_order, flight_number))

    def delete(self, stop_id):

        self.execute_non_query("DELETE FROM escale WHERE IDESC = ?", (stop_id,))


class VolDAO(DAO):#the  add vole function
    def __init__(self,db_path):
        super().__init__(db_path)  # Call the parent DAO's constructor

    def get_by_airport(self, airport_code):

        return self.execute_query("SELECT * FROM vol WHERE APORTDEP = ? OR APORTARR = ?", (airport_code, airport_code))

    def get_by_departure_time(self, hdep):

        return self.execute_query("SELECT * FROM vol WHERE HDEP = ?", (hdep,))

    def get_by_flight_duration(self, durvol):

        return self.execute_query("SELECT * FROM vol WHERE durvol = ?", (durvol,))

    def get_by_day(self, jvol):

        return self.execute_query("""SELECT * FROM vol WHERE jvol = ?""", (jvol,))
    def get_crew_by_flight_id(self,idv):
        res=self.execute_query("""SELECT NUMEMP FROM employee_vol WHERE NUMVOL=?""",idv)
        #I think on this level its safe to only work with unique attributes , hence the return of the ids of the employees & not their names !!!

    def add_crew_member(self,NUMEMP,NUMVOL):# the constraints and conditions won't be added here !! they should be placed
        # in the services.py functions & classes !!!!
        self.execute_non_query("""INSERT INTO employee_vol(NUMEMP,NUMVOL) VALUES(?,?)""",(NUMEMP,NUMVOL))


    def create(self, departure_airport, arrival_airport, departure_time,
               flight_duration, day_of_week, aircraft_id=None):

        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day_of_week not in valid_days:
            raise ValueError(f"Invalid day. Must be one of {valid_days}")

        if aircraft_id is not None:
            self.execute_non_query("""
            INSERT INTO vol (APORTDEP, APORTARR, HDEP, durvol, jvol, NUMVOL) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (departure_airport, arrival_airport, departure_time,
                  flight_duration, day_of_week, aircraft_id))
        else:
            self.execute_non_query("""
            INSERT INTO vol (APORTDEP, APORTARR, HDEP, durvol, jvol) 
            VALUES (?, ?, ?, ?, ?)
            """, (departure_airport, arrival_airport, departure_time,
                  flight_duration, day_of_week))

    def delete(self, flight_id):

        self.execute_non_query("DELETE FROM vol WHERE NUMVOL = ?", (flight_id,))













# this test function was given to me by claude !

def test_employee_dao(employee_dao):
    print("\n--- Test EmployeeDAO ---")

    # Créer un nouvel employé
    try:
        employee_dao.create(# the error in the employee is nothing to worry about !!!!! fuck this shit !!!! dy3t lwqt bzf fhad lqlawi
            email="john.doe@example.com",
            password_hash="hashed_password",
            nom="Doe",
            prenom="John",
            tel="123456789",
            ville="Paris",
            adresse="123 Rue de Paris",
            salaire=3000,
            fonction="Pilote",
            datemb="2023-01-01"
        )
        print("Employé ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'employé : {e}")

    # Récupérer par ID
    employee_id = 1  # Remplacez par l'ID correct
    print(f"Données de l'employé : {employee_dao.get_by_id(employee_id)}")

    # Mettre à jour l'adresse
    employee_dao.set_address(employee_id, "456 Nouvelle Adresse")
    print("Adresse mise à jour.")

    # Récupérer par ville
    employees_in_city = employee_dao.get_by_city("Paris")
    print(f"Employés dans la ville de Paris : {employees_in_city}")

    # Supprimer l'employé
    employee_dao.execute_non_query("DELETE FROM employees WHERE NUMEMP = ?", (employee_id,))
    print("Employé supprimé avec succès.")


def test_fl_employee_dao(fl_employee_dao):
    print("\n--- Test FL_EmployeeDAO ---")

    # Ici, vous pouvez ajouter des tests spécifiques à FL_EmployeeDAO


def test_revision_dao(revision_dao):
    print("\n--- Test RevisionDAO ---")

    # Exemple d'ajout de révision
    try:
        revision_dao.create_rev(
            report="Révision annuelle",
            daterev="2023-01-01",
            aircraft_id=1,  # Remplacez par l'ID correct
            nbhrev=100,
            tec_id=1  # Remplacez par l'ID correct
        )
        print("Révision ajoutée avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de la révision : {e}")

    # Récupérer par ID de révision
    print(f"Données de la révision : {revision_dao.get_by_revision_id(1)}")


def test_airport_dao(airport_dao):
    print("\n--- Test AirportDAO ---")

    # Ajouter un aéroport
    try:
        airport_dao.create(
            code="CDG",
            name="Charles de Gaulle",
            country="France",
            city="Roissy-en-France"
        )
        print("Aéroport ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'aéroport : {e}")

    # Récupérer un aéroport par code
    print(f"Données de l'aéroport : {airport_dao.get_by_code('CDG')}")


def test_escale_dao(escale_dao):
    print("\n--- Test EscaleDAO ---")

    # Ajouter une escale
    try:
        escale_dao.create(
            airport_code="CDG",
            arrival_time="2023-01-01 12:00:00",
            stop_duration="2h",
            flight_number="AF123",
            stop_order=1
        )
        print("Escale ajoutée avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'escale : {e}")

    # Récupérer une escale par numéro de vol
    print(f"Données de l'escale : {escale_dao.get_by_flight('AF123')}")


def test_vol_dao(vol_dao):
    print("\n--- Test VolDAO ---")

    # Ajouter un vol
    try:
        vol_dao.create(
            departure_airport="CDG",
            arrival_airport="JFK",
            departure_time="2023-01-01 10:00:00",
            flight_duration="8h",
            day_of_week="Monday"
        )
        print("Vol ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout du vol : {e}")

    # Récupérer un vol par aéroport
    print(f"Données du vol : {vol_dao.get_by_airport('CDG')}")


def main():
    # Chemin vers la base de données
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(BASE_DIR, "instance", "airplain.db")

    # Créer des instances de chaque DAO
    employee_dao = EmployeeDAO(db_path)
    fl_employee_dao = FL_EmployeeDAO(db_path)
    revision_dao = RevisionDAO(db_path)
    airport_dao = AirportDAO(db_path)
    escale_dao = EscaleDAO(db_path)
    vol_dao = VolDAO(db_path)

    # Exécuter les tests pour chaque DAO
    test_employee_dao(employee_dao)
    test_fl_employee_dao(fl_employee_dao)
    test_revision_dao(revision_dao)
    test_airport_dao(airport_dao)
    test_escale_dao(escale_dao)
    test_vol_dao(vol_dao)


if __name__ == "__main__":
    main()
