from flask import Flask,render_template,request,Blueprint,redirect,url_for
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
            crew_id2 = request.form.get("crew_id")
            Crew.create_crew(flight_id, crew_id2)
            return redirect(url_for("crew_routes.crew", action="list"))

    elif action == "update" and crew_id:
        context["crew_member"] = Crew.get_crew_by_id(crew_id)
        context["view"] = "update"
        if request.method == "POST":
            new_id = request.form.get("new_id")
            Crew.update_crew(crew_id, new_id)
            return redirect(url_for("crew_routes.crew", action="list",id=crew_id))

    elif action == "delete" and crew_id and request.method == "POST":
        Crew.delete_crew(crew_id)
        return redirect(url_for("crew_routes.crew", action="list"))    
    return render_template("crew.html", context=context)    