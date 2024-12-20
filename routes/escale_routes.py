from flask import Blueprint, render_template, request,redirect,url_for
from models.escale import Escale

escale_routes=Blueprint("escale_routes",__name__)

@escale_routes.route("/escale", methods=["GET", "POST"])
def escale():
    action = request.args.get("action", "list")
    escale_id = request.args.get("id", type=int)
    context = {}

    if action == "list":
        context["escales"] = Escale.get_all_escale()
        context["view"] = "list"

    elif action == "details" and escale_id:
        context["escale"] = Escale.get_escale_by_id(escale_id)
        context["view"] = "details"

    elif action == "search":
        if request.method == "POST":
            codev = request.form.get("CODEV")
            numvol = request.form.get("NUMVOL")
            if codev:
                context["escales"]=Escale.get_escale_by_airport(codev) 
            if numvol:
                context["escales"]=Escale.get_escale_by_numvol(numvol)
        context["view"] = "search"

    elif action == "create":
        context["view"] = "create"
        if request.method == "POST":
            airport_code = request.form.get("APORTESC")
            arrival_time = request.form.get("HARRESC")
            stop_duration = request.form.get("DURESC")
            stop_order = request.form.get("NOORD")
            flight_number = request.form.get("NUMVOL")

            if not all([airport_code, arrival_time, stop_duration, stop_order, flight_number]):
                context["error"] = "All fields are required to create an escale!"
                return render_template("escale.html", context=context)
            Escale.create_escale(airport_code, arrival_time, stop_duration, stop_order, flight_number)
            return redirect(url_for('escale_routes.escale', action='list'))

    elif action == "update" and escale_id:
        context["view"] = "update"
        context["escale"] = Escale.get_escale_by_id(escale_id)
        if request.method == "POST":
            airport_code = request.form.get("APORTESC")
            arrival_time = request.form.get("HARRESC")
            stop_duration = request.form.get("DURESC")
            stop_order = request.form.get("NOORD")

            Escale.update_escale(escale_id, airport_code, arrival_time, stop_duration, stop_order)
            return redirect(url_for('escale_routes.escale', action='details', id=escale_id))

    elif action == "delete" and escale_id and request.method == "POST":
        Escale.delete_escale(escale_id)
        return redirect(url_for('escale_routes.escale', action='list'))

    return render_template("escale.html", context=context)

@escale_routes.route("/get_dropdown_data", methods=["GET"])
def get_dropdown_data():
    field = request.args.get("field", "")

    if field == "flight":
        flights = Escale.get_all_flights()
        dropdown_data = [flight[0] for flight in flights]
    elif field == "airport":
        airports = Escale.get_all_airport_code()
        dropdown_data = [airport[0] for airport in airports]
    else:
        dropdown_data = []

    return {"dropdown_data": dropdown_data}