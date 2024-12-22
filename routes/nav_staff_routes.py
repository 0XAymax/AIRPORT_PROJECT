from flask import Blueprint, render_template, request, redirect, url_for, flash
from AIRPORT_PROJECT.models.revision import Revision
from AIRPORT_PROJECT.models.aircraft import Aircraft
from AIRPORT_PROJECT.models.emloyee import FL_Employee
from datetime import datetime, timedelta
nav_staff_routes = Blueprint('nav_staff_routes', __name__)

@nav_staff_routes.route('/schedule/<int:emp_id>', methods=["GET", "POST"])
def view_schedule(emp_id):
    schedule = FL_Employee.get_employee_schedule(emp_id)

    # Create a dictionary mapping numerical day values to day names
    days_of_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    return render_template('schedule.html',
                         schedule=schedule,
                         days_of_week=days_of_week)
