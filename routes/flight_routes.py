from flask import Flask,render_template,request,Blueprint,redirect,url_for
from models.flight import Vol
flight_routes=Blueprint("flight_routes",__name__)

@flight_routes.route("/flight", methods=["GET", "POST"])
def flight():
    action = request.args.get("action", "list")
    flight_id = request.args.get("id", type=int)
    departure = request.form.get("departure", "")
    day = request.form.get("day","")
    depart=request.form.get("depart","")
    hddep=request.form.get("hddep","")
    context = {}

    if action == "list":
        context["flights"] = Vol.get_all_vol()
        context["total_flights"] = Vol.count_flights()
        context["view"] = "list"

    elif action == "details" and flight_id:
        context["flight"] = Vol.get_vol(flight_id)
        context["view"] = "details"
        
    elif action == "search":
        if request.method == "POST":
            if day:
             context["flights"] = Vol.get_vol_by_day(day)
            if depart: 
             context["flights"] = Vol.get_vol_by_depart(depart)
            if hddep:
              context["flights"] = Vol.get_vol_by_hdep(hddep) 
        context["view"] = "search"

    elif action == "create":
        context["view"] = "create"
        if request.method == "POST":
            departure_airport = request.form.get("departure")
            arrival_airport = request.form.get("destination")
            departure_time = request.form.get("depart_time")
            flight_duration = request.form.get("duration")
            day_of_week = request.form.get("day")

            if not all([departure_airport, arrival_airport, departure_time, flight_duration, day_of_week]):
                context["error"] = "All fields except are required!"
                return render_template("flight.html", context=context)

            Vol.create_vol(departure_airport, arrival_airport, departure_time, 
                         flight_duration, day_of_week)
            return redirect(url_for('flight_routes.flight', action='list'))

    elif action == "update":
        context["view"] = "update"
        context["flight"] = Vol.get_vol(flight_id)
        if request.method == "POST":
            aportdep = request.form.get("departure")
            aportarr = request.form.get("destination") 
            hdep = request.form.get("hdep")
            durvol = request.form.get("duration")
            jvol = request.form.get("date")

            Vol.update_vol(flight_id, aportdep, aportarr, hdep, durvol, jvol)
            return redirect(url_for('flight_routes.flight', action='details', id=flight_id))

    elif action == "delete" and flight_id and request.method == "POST":
        Vol.delete_vol(flight_id)
        return redirect(url_for('flight_routes.flight', action='list'))
    
    
    return render_template("flight.html", context=context)

