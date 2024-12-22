import sqlite3
result ={}
conn=sqlite3.connect('airplain.db')
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
cursor.execute(query,(3,))
result = cursor.fetchall()
conn.close()
for flight in result:
    print(flight.flight_number)