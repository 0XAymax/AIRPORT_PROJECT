from flask import Blueprint, render_template, request,redirect,url_for
from models.employee import Employee
TEC_routes = Blueprint('TEC_routes',__name__)
@TEC_routes.route("",methodes=["GET","POST"])
#def X_nqme()...................
