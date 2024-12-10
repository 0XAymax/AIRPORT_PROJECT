import sqlite3
from datetime import datetime
con = sqlite3.connect("airplain.db")
cursor = con.cursor()

cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (1, 'Boeing 747', '2020-01-15', 500, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (2, 'Airbus A320', '2021-06-20', 200, 'In Maintenance')
""")

# Insert data into employees
cursor.execute("""
    INSERT INTO employees (NUMEMP, NOM, prenom, email, password, tel, ville, adresse, salaire, FONCTION, datemb)
    VALUES (1, 'Smith', 'John', 'john.smith@example.com', 'password123', 1234567890, 'New York', '123 Street A', 75000, 'Technician', '2018-05-10')
""")
cursor.execute("""
    INSERT INTO employees (NUMEMP, NOM, prenom, email, password, tel, ville, adresse, salaire, FONCTION, datemb)
    VALUES (2, 'Doe', 'Jane', 'jane.doe@example.com', 'securepass', 9876543210, 'Los Angeles', '456 Avenue B', 80000, 'Pilot', '2017-09-25')
""")

# Insert data into airport
cursor.execute("""
    INSERT INTO airport (CODEV, NOM, Pays, VILLE)
    VALUES ('JFK', 'John F. Kennedy International', 'USA', 'New York')
""")
cursor.execute("""
    INSERT INTO airport (CODEV, NOM, Pays, VILLE)
    VALUES ('LAX', 'Los Angeles International', 'USA', 'Los Angeles')
""")
cursor.execute("""
    INSERT INTO airport (CODEV, NOM, Pays, VILLE)
    VALUES ('LHR', 'London Heathrow', 'UK', 'London')
""")

# Insert data into vol
cursor.execute("""
    INSERT INTO vol (NUMVOL, APORTDEP, APORTARR, HDEP, durvol, jvol)
    VALUES (101, 'JFK', 'LAX', '08:00:00', 360, 'Monday')
""")
cursor.execute("""
    INSERT INTO vol (NUMVOL, APORTDEP, APORTARR, HDEP, durvol, jvol)
    VALUES (102, 'LAX', 'LHR', '12:30:00', 600, 'Tuesday')
""")

# Insert data into escale
cursor.execute("""
    INSERT INTO escale (IDESC, APORTESC, HARMESC, DURESC, NOORD, NUMVOL)
    VALUES (1, 'LHR', '14:00:00', '01:30:00', 1, 102)
""")

# Insert data into revision
cursor.execute("""
    INSERT INTO revision (NUMREV, RAPPPORT, DATEREV, NBHREV, NUMAV, TECID)
    VALUES (1, 'Routine maintenance completed.', '2023-10-12', 4, 1, 1)
""")

# Insert data into employee_vol (many-to-many relationship)
cursor.execute("""
    INSERT INTO employee_vol (NUMEMP, NUMVOL)
    VALUES (2, 101)
""")
cursor.execute("""
    INSERT INTO employee_vol (NUMEMP, NUMVOL)
    VALUES (2, 102)
""")

# Commit changes and close the connection
con.commit()
con.close()

print("Data inserted successfully!")
