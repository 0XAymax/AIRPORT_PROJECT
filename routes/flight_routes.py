from flask import Flask,render_template,request,Blueprint,redirect,url_for,jsonify
from models.flight import Vol
flight_routes=Blueprint("flight_routes",__name__)

def get_aircraft_dropdown_data():
    aircrafts = Vol.get_all_aircraft_ID()  # Fetch aircraft data from DB
    if not aircrafts:
        return []  # Return empty list if no aircraft data found
    return aircrafts  # Return aircraft data if found



@flight_routes.route("/flight", methods=["GET", "POST"])
def flight():
    action = request.args.get("action", "list")
    flight_id = request.args.get("id", type=int)
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
             context["flights"] = Vol.get_all_vol_by_depart(depart)
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
            numv=Vol.get_aircraft_by_name(numv)
            departure_airport=Vol.get_airport_code_by_name(departure_airport)
            arrival_airport=Vol.get_airport_code_by_name(arrival_airport)
            Vol.create_vol(numv,departure_airport, arrival_airport, departure_time, 
                         flight_duration, day_of_week)
            return redirect(url_for('flight_routes.flight', action='list'))

    elif action == "update":
        context["view"] = "update"
        context["flight"] = Vol.get_vol(flight_id)
        if request.method == "POST":
            numav=request.form.get("numav")
            aportdep = request.form.get("departure")
            aportarr = request.form.get("destination") 
            hdep = request.form.get("hdep")
            durvol = request.form.get("duration")
            jvol = request.form.get("date")
            
            if numav:
                numav=Vol.get_aircraft_by_name(numav)
            if aportdep:
                aportdep=Vol.get_airport_code_by_name(aportdep)
            if aportarr:
                aportarr=Vol.get_airport_code_by_name(aportarr)        
            Vol.update_vol(flight_id,numav, aportdep, aportarr, hdep, durvol, jvol)
            return redirect(url_for('flight_routes.flight', action='details', id=flight_id))

    elif action == "delete" and flight_id and request.method == "POST":
        Vol.delete_vol(flight_id)
        return redirect(url_for('flight_routes.flight', action='list'))
    
    return render_template("flight.html", context=context)

def get_dropdown_data():
    field = request.args.get('field')
    print(f"Received field: {field}")  # Debug the received field

    if field == "aircraft":
        # Get aircraft dropdown data using the helper function
        dropdown_data = get_aircraft_dropdown_data()
    elif field == "airport":
        airports = Vol.get_all_airports_name()
        print(f"Airports fetched from DB: {airports}")  # Debug DB response
        dropdown_data = [airport[0] for airport in airports]
    else:
        dropdown_data = []

    print(f"Dropdown Data: {dropdown_data}")  # Debug final data
    return jsonify({"dropdown_data": dropdown_data})

@flight_routes.route("/get_aircraft_dropdown", methods=["GET"])
def get_aircraft_dropdown():
    try:
        aircrafts = Vol.get_all_aircraft_ID() 

        if not aircrafts:
            raise ValueError("No aircraft available")

        return jsonify({"dropdown_data": aircrafts})  

    except Exception as e:
        print(f"Error in /get_aircraft_dropdown route: {e}")
        return jsonify({"error": str(e)}), 500  
