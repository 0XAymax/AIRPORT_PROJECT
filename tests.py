import sqlite3

# Connect to the database
con = sqlite3.connect('airplain.db')
cursor = con.cursor()

# Execute the query
cursor.execute("""
    SELECT email, password, FONCTION 
    FROM employees
""")

# Fetch the results
results = cursor.fetchall()

# Print the results
for email, password, fonction in results:
    print(f"Email: {email}, Password: {password}, Function: {fonction}")

# Close the connection
con.close()


