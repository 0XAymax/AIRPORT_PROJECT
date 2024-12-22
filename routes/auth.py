from flask import Blueprint, render_template, flash, redirect, url_for, session
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
            session['user_role'] = user['FONCTION']  

            if user['FONCTION'] == 'Admin':
                return redirect(url_for('auth.home'))
            elif user['FONCTION'] == 'Flight Manager':
                return redirect(url_for('auth.flight_manager'))
            elif user['FONCTION'] == 'Human Ressources Manager':
                return redirect(url_for('hr_routes.hr'))
            elif user['FONCTION'] == 'Technician':
                return redirect(url_for('maintanance_routes.maintenance'))
            elif user['FONCTION']=='Pilot' or user['FONCTION']=='Flight Attendant':
                return redirect(url_for('nav_staff_routes.view_schedule', emp_id=session['user_id']))
            else:
                flash('Access denied. You do not have the required permissions.', 'danger')
                return redirect(url_for('auth.login'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)

# Home route for admin
@auth_blueprint.route("/home")
def home():
    if 'user_role' in session and session['user_role'] == 'Admin':
        return render_template('home.html')
    else:
        flash('Access denied. Admins only.', 'danger')
        return redirect(url_for('auth.login'))

# Flight manager route
@auth_blueprint.route("/flight_manager")
def flight_manager():
    if 'user_role' in session and session['user_role'] == 'Flight Manager':
        return render_template('flight_manager.html')
    else:
        flash('Access denied. Flight managers only.', 'danger')
        return redirect(url_for('auth.login'))
    
@auth_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)  
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))     