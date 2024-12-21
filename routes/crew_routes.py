from flask import render_template,request,Blueprint,redirect,url_for
from models.crew import Crew

crew_routes=Blueprint("crew_routes",__name__)

@crew_routes.route("/crew",methods=["GET","POST"])
def crew():
    action = request.args.get("action", "list")
    crew_id = request.args.get("id", type=int)
    context = {}

    if action == "list":
        context["crew"] = Crew.get_all_crew()
        context["view"] = "crew_list"

    elif action == "details" and crew_id:
        context["crew_member"] = Crew.get_crew_by_id(crew_id)
        context["view"] = "details"

    elif action == "create":
        context["view"] = "create"
        if request.method == "POST":
            flight_id = request.form.get("flight_id") 
            nom=request.form.get("nom")
            prenom=request.form.get("prenom")
            email=request.form.get("email")
            passw=request.form.get("password")
            tel=request.form.get("tel")
            ville=request.form.get("ville")
            address=request.form.get("adresse")
            salaire=request.form.get("salaire")
            function=request.form.get("function")
            datemb=request.form.get("datemb")
            if Crew.check_email_exists(email):
                context["error"]="Email Already Exists !"
                return render_template("crew.html",context)
            if not all([flight_id,nom,prenom,email,passw,tel,ville,address,salaire,function,datemb]):
                context["error2"] = "All fields except are required!"
                return render_template("crew.html", context=context)
            Crew.create_crew(email,passw,nom,prenom,tel,ville,address,salaire,function,datemb)
            Crew.insert_crew_member(email,flight_id)
            return redirect(url_for("crew_routes.crew", action="list"))

    elif action == "update" and crew_id:
        context["crew_member"] = Crew.get_crew_by_id(crew_id)
        context["view"] = "update"
        if request.method == "POST":
            new_id = request.form.get("flight_id")
            new_name=request.form.get("new_nom")
            new_prenom=request.form.get("new_prenom")
            new_email=request.form.get("new_email")
            new_password=request.form.get("new_password")
            new_tel=request.form.get("new_tel")
            new_ville=request.form.get("new_ville")
            new_address=request.form.get("new_adresse")
            new_salaire=request.form.get("new_salaire")
            new_function=request.form.get("new_function")
            new_datemb=request.form.get("new_datemb")

            Crew.update_crew(crew_id, new_id,new_name,new_prenom,new_email,new_password,new_tel,new_ville,new_address,new_salaire,new_function,new_datemb)
            return redirect(url_for("crew_routes.crew", action="list",id=crew_id))

    elif action == "delete" and crew_id and request.method == "POST":
        Crew.delete_crew(crew_id)
        return redirect(url_for("crew_routes.crew", action="list"))    
    return render_template("crew.html", context=context)    

@crew_routes.route("/get_dropdown_data", methods=["GET"])
def get_dropdown_data():
    field = request.args.get("field", "")

    if field == "flight":
        flights = Crew.get_all_flights()
        dropdown_data = [flight[0] for flight in flights]
    else:
        dropdown_data = []

    return {"dropdown_data": dropdown_data}