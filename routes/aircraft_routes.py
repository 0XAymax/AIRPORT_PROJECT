from flask import Blueprint, render_template, request
from models.aircraft import Aircraft

aircraft_routes = Blueprint('aircraft_routes', __name__)

@aircraft_routes.route("/aircraft", methods=["GET", "POST"])
def aircraft():
    action = request.args.get("action", "list")
    aircraft_id = request.args.get("id", type=int)
    name = request.form.get("name", "")
    context = {}

    if action == "list":
        context["aircrafts"] = Aircraft.get_all_aircrafts()
        context["view"] = "list"
    elif action == "details" and aircraft_id:
        context["aircraft"] = Aircraft.get_by_id(aircraft_id)
        context["view"] = "details"
    elif action == "status" and aircraft_id:
        context["status"] = Aircraft.get_status(aircraft_id)
        context["view"] = "status"
    elif action == "search":
        if request.method == "POST":
            context["aircrafts"] = Aircraft.get_by_name(name)
        context["view"] = "search"
    elif action == "nbhddrev" and aircraft_id:
        context["nbhddrev"] = Aircraft.get_nbhddrev(aircraft_id)
        context["view"] = "nbhddrev"
    elif action == "datems" and aircraft_id:
        context["datems"] = Aircraft.get_datems(aircraft_id)
        context["view"] = "datems"

    return render_template("aircraft.html", context=context)


