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
            if not Escale.check_airport_exists(airport_code):
                context["error2"] ="Airport code doesn't exists!,check airports"
                return render_template("escale.html", context=context)
            if not Escale.check_flight_exists(flight_number):
                context["error4"]="Flight ID doesn't exists !"
                return render_template("escale.html",context=context)
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

            if not Escale.check_airport_exists(airport_code):
                context["error3"] ="Airport code doesn't exists!,check airports"
                return render_template("escale.html", context=context)
            Escale.update_escale(escale_id, airport_code, arrival_time, stop_duration, stop_order)
            return redirect(url_for('escale_routes.escale', action='details', id=escale_id))

    elif action == "delete" and escale_id and request.method == "POST":
        Escale.delete_escale(escale_id)
        return redirect(url_for('escale_routes.escale', action='list'))

    return render_template("escale.html", context=context)
