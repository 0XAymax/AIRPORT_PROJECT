from flask import Flask, render_template,flash,url_for,redirect
from login_form import loginform 
import os
import sqlite3


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback_secret_key')  

def get_db_connection():
    conn = sqlite3.connect('biblio.db')
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/", methods=["GET", "POST"])  
def login():
    form = loginform()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        conn = sqlite3.connect('biblio.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard')) 
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the dashboard!</h1>"
if __name__ == '__main__':
    app.run(debug=True)

