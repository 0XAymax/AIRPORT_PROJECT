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
            numv=request.form.get("numav")
            departure_airport = request.form.get("departure")
            arrival_airport = request.form.get("destination")
            departure_time = request.form.get("depart_time")
            flight_duration = request.form.get("duration")
            day_of_week = request.form.get("day")

            if not all([departure_airport, arrival_airport, departure_time, flight_duration, day_of_week]):
                context["error"] = "All fields except are required!"
                return render_template("flight.html", context=context)
            if not Vol.check_airport_exists(departure_airport):
               context["error2"]="Departure airport code doesn't exists !,check airports !"
               return render_template("flight.html",context=context)
            if not Vol.check_airport_exists(arrival_airport):
               context["error5"]="Arrive airport code doesn't exists !,check airports !"
               return render_template("flight.html",context=context)
            if not Vol.aircraft_exists(numv):
               context["error6"]="Aircraft ID doesn't exists !,check aircrafts !"
               return render_template("flight.html",context=context)
            if Vol.aircraft_is_available(numv) != 'Available' :
               context["available"]="Aircraft is "+Vol.aircraft_is_available(numv)+" !"
               return render_template("flight.html",context=context)
            Vol.create_vol(numv,departure_airport, arrival_airport, departure_time, 
                         flight_duration, day_of_week)
            return redirect(url_for('flight_routes.flight', action='list'))

    elif action == "update":
        context["view"] = "update"
        context["flight"] = Vol.get_vol(flight_id)
        if request.method == "POST":
            numaav=request.form.get("numaav")
            aportdep = request.form.get("departure")
            aportarr = request.form.get("destination") 
            hdep = request.form.get("hdep")
            durvol = request.form.get("duration")
            jvol = request.form.get("date")
            if aportdep:
             if not Vol.check_airport_exists(aportdep):
               context["error3"]="Departure airport code doesn't exists !,check airports !"
               return render_template("flight.html",context=context)
            if aportarr:
               if not Vol.check_airport_exists(aportarr):
                   context["error4"]=" Arrive airport code doesn't exists !,check airports !"
                   return render_template("flight.html",context=context)
            if numaav:
               if not Vol.aircraft_exists(numaav):
                 context["error8"]="Aircraft ID doesn't exists !,check aircrafts !"
                 return render_template("flight.html",context=context)
               if Vol.aircraft_is_available(numaav) != 'Available' :
                 context["available2"]="Aircraft is "+Vol.aircraft_is_available(numaav)+" !"
                 return render_template("flight.html",context=context)
            Vol.update_vol(numaav,flight_id, aportdep, aportarr, hdep, durvol, jvol)
            return redirect(url_for('flight_routes.flight', action='details', id=flight_id))

    elif action == "delete" and flight_id and request.method == "POST":
        Vol.delete_vol(flight_id)
        return redirect(url_for('flight_routes.flight', action='list'))
    
    
    return render_template("flight.html", context=context)

