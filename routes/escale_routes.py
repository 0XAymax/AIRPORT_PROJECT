from flask import Blueprint, render_template, request,redirect,url_for
from models.escale import Escale

escale_routes=Blueprint("escale_routes",__name__)

@escale_routes.route("/escale",methods=["GET" ,"POST"])
def escale():
    action=request.args.get("action","list")
    idesc=request.args.get("id" ,type=int)
    codev=request.form.get("CODEV" ,"")
    numvol = request.form.get("NUMVOL", "")
    context ={}

    if action == "list":
        context["escales"]=Escale.get_all_escale()
        context["view"]="list"
    elif action == "details" and idesc:
        context["escale"] = Escale.get_escale_by_id(idesc)
        context["view"] = "details"
    elif action == "search":
        if request.method == "POST":
            escales_by_numvol = Escale.get_escale_by_numvol(numvol) if numvol else None
            escales_by_airport = Escale.get_escale_by_airport(codev) if codev else None
            
            context["escales"] = []
            if escales_by_numvol:
               context["escales"].extend(escales_by_numvol if isinstance(escales_by_numvol, list) else [escales_by_numvol])
            if escales_by_airport:
               context["escales"].extend(escales_by_airport if isinstance(escales_by_airport, list) else [escales_by_airport])
            if not context["escales"]:
              context["message"] = "No escales found for the given criteria."

        context["view"] = "search"
    elif action == "arrival_time" and idesc:
        arrival_time = Escale.get_heure_arrive(idesc)
        if arrival_time:
           context["arrival_time"] = arrival_time
        else:
           context["message"] = "No arrival time found for the specified escale."
        context["view"] = "arrival_time"    
    elif action == "create":
        context["view"] = "create"
        if request.method == "POST":
            airport_code = request.form.get("APORTESC")
            arrival_time = request.form.get("HARRESC")
            stop_duration = request.form.get("DURESC")
            stop_order = request.form.get("NOORD")
            flight_number = request.form.get("NUMVOL")

            if not airport_code or not arrival_time or not stop_duration or not stop_order or not flight_number:
                context["error"] = "All fields are required!"
                return render_template("escale.html", context=context)

            Escale.create_escale(airport_code, arrival_time, stop_duration, stop_order, flight_number)
            return redirect(url_for('escale_routes.escale', action='list'))
    elif action == "update":
        context["view"]="update"
        context["escale"]=Escale.get_escale_by_id(idesc)
        if request.method == "POST":
            new_aportesc =request.form.get("aportesc")
            new_harresc =request.form.get("harresc")
            new_duresc=request.form.get("duresc")
            new_noord=request.form.get("noord")

            Escale.update_escale(idesc,new_aportesc,new_harresc,new_duresc,new_noord)
            return redirect(url_for('escale_routes.escale',action='details',id=idesc))
    elif action == "delete" and idesc and request.method == "POST":
        Escale.delete_escale(idesc)
        return redirect(url_for('escale_routes.escale', action='list'))

    return render_template("escale.html", context=context)
