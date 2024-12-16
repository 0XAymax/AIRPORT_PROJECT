from flask import Blueprint, render_template, request,redirect,url_for
from models.employee import Employee
HR_routes = Blueprint('HR_routes',__name__)
@HR_routes.route("",methodes=["GET","POST"])
#def X_nqme()
