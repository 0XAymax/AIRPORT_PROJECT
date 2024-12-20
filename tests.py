import sqlite3


con = sqlite3.connect("airplain.db")
cursor = con.cursor()
'''
cursor.execute("""
    SELECT 
    employee_vol.NUMEMP AS employee_id,
    employees.NOM AS name,
    employees.prenom AS last_name,
    employees.email AS email,
    employee_vol.NUMVOL AS flight_number
FROM 
    employee_vol
INNER JOIN 
    employees ON employee_vol.NUMEMP = employees.NUMEMP
INNER JOIN 
    flight ON employee_vol.NUMVOL = flight.id;
""")
'''
cursor.execute("""
SELECT 
    ev.NUMEMP AS employee_id,
    e.NOM AS name,
    e.prenom AS last_name,
    e.email AS email,
    f.NUMVOL AS flight_number,
    f.APORTDEP AS departure_airport,
    f.APORTARR AS arrival_airport,
    f.HDEP AS departure_time
FROM 
    employee_vol ev
JOIN 
    employees e ON ev.NUMEMP = e.NUMEMP
JOIN 
    flight f ON ev.NUMVOL = f.id;
"""
 )
rows=cursor.fetchall()
con.close()
print(rows)