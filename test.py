from flask import Flask, render_template
import mysql.connector
import sqlite3

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='yourdbname'
    )
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
