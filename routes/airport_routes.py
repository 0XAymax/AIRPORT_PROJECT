from flask import Blueprint, render_template, request,redirect,url_for
from AIRPORT_PROJECT.models.airport import Airport

airport_routes = Blueprint('airport_routes',__name__)

@airport_routes.route("/airport",methods=["GET", "POST"])
def airport():
    action = request.args.get("action", "list")
    airport_id = request.args.get("id", type=str)
    name = request.form.get("name", "")
    city =request.form.get("city","")
    context = {}

    if action=="list":
        context["airports"]=Airport.get_all()
        context["view"]="list"
    elif action == "details" and airport_id:
        context["airport"]=Airport.get_airport_by_id(airport_id)
        context["view"]="details"
    elif action == "search":
        if request.method == "POST":
            if name:
              context["airports"] =Airport.get_airport_by_name(name)
            if city:
              context["airports"]=Airport.get_airport_by_city(city)  
        context["view"]= "search"
    elif action == "city" and airport_id:
        context["city"]=Airport.get_city(airport_id)  
        context["view"]="city"
    elif action == "create" :
        context["view"]="create"
        if request.method == "POST":
            codev=request.form.get("codev")
            nom=request.form.get("nom")
            pays=request.form.get("pays")
            ville=request.form.get("ville")

            if not codev or not nom or not pays or not ville:
                context["error"]="All fields are required!"
                return render_template("airport.html",context=context)
            
            Airport.create_airport(codev,nom,pays,ville)
            return redirect(url_for('airport_routes.airport',action='list'))
    elif action == "update" :
        context["view"]="update"
        context["airport"]=Airport.get_airport_by_id(airport_id)
        if request.method == "POST":
            new_name =request.form.get("nom")
            new_pays =request.form.get("pays")
            new_city=request.form.get("ville")    

            Airport.update_airport(airport_id,new_name,new_pays,new_city)
            return redirect(url_for('airport_routes.airport',action='details',id=airport_id))

    elif action== "delete" and airport_id and request.method == "POST":
        Airport.delete_airport(airport_id)
        return redirect(url_for('airport_routes.airport',action='list'))
    
    return render_template("airport.html",context=context)


