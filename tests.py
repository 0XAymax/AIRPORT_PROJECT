import sqlite3
from datetime import datetime
from models.crew import Crew
con = sqlite3.connect("airplain.db")
cursor = con.cursor()
context={}
email ="hamza@gmail.com"
flight_id=3
Crew.insert_crew_member(email,flight_id)
    