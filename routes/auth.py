from flask import Blueprint, render_template, flash, redirect, url_for
from login_form import loginform  
import sqlite3

# Define a blueprint for authentication routes
auth_blueprint = Blueprint('auth', __name__)

# Function to get the database connection
def get_db_connection():
    conn = sqlite3.connect('airplain.db')
    conn.row_factory = sqlite3.Row
    return conn

# Login route
@auth_blueprint.route("/", methods=["GET", "POST"])
def login():
    form = loginform()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard')) 
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)

# Dashboard route
@auth_blueprint.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the dashboard!</h1>"
