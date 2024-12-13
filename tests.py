import sqlite3
from datetime import datetime
con = sqlite3.connect("airplain.db")
cursor = con.cursor()

cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (3, 'Cessna 172', '2019-11-05', 3000, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (4, 'Boeing 747', '2017-01-22', 2200, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (5, 'Airbus A380', '2022-03-18', 50, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (6, 'Bombardier CRJ700', '2015-09-12', 4200, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (7, 'Embraer E190', '2021-07-30', 300, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (8, 'Boeing 777', '2016-12-25', 1800, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (9, 'Concorde', '2000-08-14', 5200, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (10, 'Boeing 767', '2019-02-28', 1300, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (11, 'Lockheed L-1011 TriStar', '1995-04-10', 7000, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (12, 'McDonnell Douglas MD-80', '2010-06-15', 4600, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (13, 'ATR 72', '2021-01-01', 100, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (14, 'Boeing 787 Dreamliner', '2023-02-20', 20, 'Available')
""")
cursor.execute("""
    INSERT INTO aircraft (NUMAV, TYPE, datems, NBHDDREV, status)
    VALUES (15, 'Airbus A330', '2018-11-09', 1600, 'Available')
""")

# Commit changes and close the connection
con.commit()
con.close()

print("Data inserted successfully!")
