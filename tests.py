import sqlite3
from datetime import datetime, time

# Connect to database
conn = sqlite3.connect('airplain.db')
cursor = conn.cursor()

# Aircraft data
aircraft_data = [
    ('Boeing 737-800', '2018-03-15', 3500, 'Available'),
    ('Airbus A320', '2019-06-22', 2800, 'Available'),
    ('Boeing 777-300ER', '2017-11-30', 4200, 'In Maintenance'),
    ('Airbus A350-900', '2020-01-10', 1500, 'Available'),
    ('Boeing 787-9', '2019-08-05', 2100, 'ReqMaintenance'),
    ('Airbus A330-300', '2016-12-18', 5600, 'Available'),
    ('Boeing 747-8', '2015-07-25', 6800, 'Out of Service'),
    ('Airbus A380', '2017-04-30', 4900, 'Available'),
    ('Boeing 767-300ER', '2016-09-12', 5300, 'In Maintenance'),
    ('Airbus A321neo', '2021-02-28', 800, 'Available')
]

cursor.executemany("""
    INSERT INTO aircraft (TYPE, datems, NBHDDREV, status)
    VALUES (?, ?, ?, ?)
""", aircraft_data)

# Employees data
employees_data = [
    ('Smith', 'John', 'john.smith@airline.com', 'hash1234', 5551234567, 'New York', '123 Aviation St', 85000.00, 'Pilot', '2018-06-15', 3500, 4000),
    ('Johnson', 'Sarah', 'sarah.j@airline.com', 'hash2345', 5552345678, 'Chicago', '456 Flight Ave', 78000.00, 'Pilot', '2019-03-22', 2800, 3200),
    ('Williams', 'Michael', 'michael.w@airline.com', 'hash3456', 5553456789, 'Los Angeles', '789 Plane Rd', 65000.00, 'Flight Attendant', '2020-01-10', None, None),
    ('Brown', 'Emma', 'emma.b@airline.com', 'hash4567', 5554567890, 'Houston', '321 Airport Blvd', 72000.00, 'Technician', '2017-11-30', None, None),
    ('Davis', 'James', 'james.d@airline.com', 'hash5678', 5555678901, 'Miami', '654 Terminal Dr', 95000.00, 'Flight Manager', '2016-08-15', None, None),
    ('Garcia', 'Maria', 'maria.g@airline.com', 'hash6789', 5556789012, 'Dallas', '987 Hangar Way', 60000.00, 'Flight Attendant', '2019-05-20', None, None),
    ('Miller', 'David', 'david.m@airline.com', 'hash7890', 5557890123, 'Seattle', '147 Wing St', 82000.00, 'Pilot', '2017-12-05', 4100, 4500),
    ('Wilson', 'Lisa', 'lisa.w@airline.com', 'hash8901', 5558901234, 'Boston', '258 Cockpit Ln', 115000.00, 'Admin', '2015-03-18', None, None),
    ('Anderson', 'Robert', 'robert.a@airline.com', 'hash9012', 5559012345, 'Phoenix', '369 Runway Rd', 68000.00, 'Technician', '2018-09-30', None, None),
    ('Taylor', 'Jennifer', 'jennifer.t@airline.com', 'hash0123', 5550123456, 'Denver', '741 Sky Ave', 71000.00, 'Flight Attendant', '2020-02-14', None, None),
    ('Thomas', 'William', 'william.t@airline.com', 'hash1122', 5551122334, 'Atlanta', '852 Cloud St', 88000.00, 'Pilot', '2016-11-08', 5200, 5800),
    ('Moore', 'Patricia', 'patricia.m@airline.com', 'hash2233', 5552233445, 'San Francisco', '963 Jet Way', 64000.00, 'Flight Attendant', '2019-07-25', None, None),
    ('Jackson', 'Richard', 'richard.j@airline.com', 'hash3344', 5553344556, 'Las Vegas', '159 Engine Rd', 73000.00, 'Technician', '2018-04-12', None, None),
    ('White', 'Elizabeth', 'elizabeth.w@airline.com', 'hash4455', 5554455667, 'Orlando', '357 Pilot Ave', 92000.00, 'Human Ressources Manager', '2017-01-30', None, None),
    ('Harris', 'Charles', 'charles.h@airline.com', 'hash5566', 5555566778, 'Minneapolis', '456 Control St', 79000.00, 'Pilot', '2019-10-15', 2900, 3300),
    ('Martin', 'Susan', 'susan.m@airline.com', 'hash6677', 5556677889, 'Detroit', '789 Terminal Way', 67000.00, 'Flight Attendant', '2020-03-08', None, None),
    ('Thompson', 'Joseph', 'joseph.t@airline.com', 'hash7788', 5557788990, 'Portland', '147 Aviation Park', 70000.00, 'Technician', '2018-08-22', None, None),
    ('Lee', 'Margaret', 'margaret.l@airline.com', 'hash8899', 5558899001, 'San Diego', '258 Flight Line', 86000.00, 'Flight Manager', '2016-05-17', None, None),
    ('Clark', 'Thomas', 'thomas.c@airline.com', 'hash9900', 5559900112, 'Austin', '369 Airplane St', 63000.00, 'Flight Attendant', '2019-12-01', None, None),
    ('Rodriguez', 'Daniel', 'daniel.r@airline.com', 'hash0011', 5550011223, 'Philadelphia', '741 Boeing Ave', 76000.00, 'Pilot', '2017-09-14', 3800, 4200)
]

cursor.executemany("""
    INSERT INTO employees (NOM, prenom, email, password, tel, ville, adresse, salaire, FONCTION, datemb, NBMHV, NBTHV)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", employees_data)

# Revision data
revision_data = [
    ('Annual maintenance completed - all systems checked', '2023-12-15', 48, 1, 4),
    ('Engine inspection and minor repairs', '2023-11-20', 24, 2, 9),
    ('Routine maintenance and systems update', '2023-10-05', 36, 3, 13),
    ('Emergency landing gear inspection', '2023-09-18', 12, 4, 17),
    ('Complete avionics system overhaul', '2023-08-30', 72, 5, 4),
    ('Fuel system maintenance and testing', '2023-07-25', 18, 6, 9),
    ('Cabin pressurization system check', '2023-06-12', 24, 7, 13),
    ('Regular maintenance and safety inspection', '2023-05-08', 30, 8, 17),
    ('Wing structure inspection and repair', '2023-04-15', 40, 9, 4),
    ('Environmental control system maintenance', '2023-03-20', 16, 10, 9)
]

cursor.executemany("""
    INSERT INTO revision (RAPPPORT, DATEREV, NBHREV, NUMAV, TECID)
    VALUES (?, ?, ?, ?, ?)
""", revision_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data successfully inserted into the database!")
