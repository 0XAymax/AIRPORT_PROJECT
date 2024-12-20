from flask import Blueprint, render_template, flash, redirect, url_for,session
from login_form import loginform  
import sqlite3

# Define a blueprint for authentication routes
auth_blueprint = Blueprint('auth', __name__)

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
            session['user_id'] = user['NUMEMP']
            return redirect(url_for('auth.home')) 
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)

# Dashboard route
@auth_blueprint.route('/home')
def home():
    return render_template("home.html")

@auth_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)  
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login')) 