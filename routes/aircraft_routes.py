from flask import Blueprint, render_template, request,redirect,url_for
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
        
    elif action == "create" :
        context["view"]="create"
        if request.method == "POST":
          aircraft_type = request.form.get("type")
          datems = request.form.get("datems")
          nbhddrev = request.form.get("nbhddrev")
          status = request.form.get("status")

          if not aircraft_type or not datems or not nbhddrev or not status:
                context["error"] = "All fields are required!"
                return render_template("aircraft.html", context=context)
        
          Aircraft.create_aircraft( aircraft_type, datems, nbhddrev, status)
          return redirect(url_for('aircraft_routes.aircraft', action='list'))
    

    elif action == "update" and aircraft_id:
        context["aircraft"] = Aircraft.get_by_id(aircraft_id)
        context["view"]="update"
        if request.method == "POST":
          aircraft_type = request.form.get("type")
          datems = request.form.get("datems")
          nbhddrev = request.form.get("nbhddrev")
          status = request.form.get("status")
        
          Aircraft.update_aircraft(aircraft_id, aircraft_type, datems, nbhddrev, status)
          return redirect(url_for('aircraft_routes.aircraft', action='details', id=aircraft_id))
    
    elif action == "delete" and aircraft_id and request.method == "POST":
        Aircraft.delete_aircraft(aircraft_id)
        return redirect(url_for('aircraft_routes.aircraft', action='list'))
    

    return render_template("aircraft.html", context=context)


