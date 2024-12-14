from flask import Blueprint, render_template, request,redirect,url_for
from models.escale import Escale

escale_routes=Blueprint("escale_routes",__name__)

@escale_routes.route("/escale", methods=["GET", "POST"])
def escale():
    context = {
        "escales": Escale.get_all_escale(),
        "message": "",
    }

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create":
            # Handle create escale
            airport_code = request.form.get("APORTESC")
            arrival_time = request.form.get("HARRESC")
            stop_duration = request.form.get("DURESC")
            stop_order = request.form.get("NOORD")
            flight_number = request.form.get("NUMVOL")

            if not all([airport_code, arrival_time, stop_duration, stop_order, flight_number]):
                context["message"] = "All fields are required to create an escale!"
            else:
                Escale.create_escale(airport_code, arrival_time, stop_duration, stop_order, flight_number)
                context["message"] = "Escale created successfully!"
        
        elif action == "search":
            # Handle search escale
            codev = request.form.get("CODEV")
            numvol = request.form.get("NUMVOL")
            search_results = []

            if codev:
                search_results.extend(Escale.get_escale_by_airport(codev) or [])
            if numvol:
                result = Escale.get_escale_by_numvol(numvol)
                if result:
                    search_results.append(result)

            if search_results:
                context["escales"] = search_results
                context["message"] = f"Found {len(search_results)} escale(s)."
            else:
                context["message"] = "No escales found matching the search criteria."
        
        elif action == "delete":
            # Handle delete escale
            idesc = request.form.get("IDESC")
            if idesc:
                Escale.delete_escale(idesc)
                context["message"] = "Escale deleted successfully!"
            else:
                context["message"] = "IDESC is required to delete an escale."

        elif action == "update":
            # Handle update escale
            idesc = request.form.get("IDESC")
            aportesc = request.form.get("APORTESC")
            harresc = request.form.get("HARRESC")
            duresc = request.form.get("DURESC")
            noord = request.form.get("NOORD")

            if idesc:
                Escale.update_escale(idesc, aportesc, harresc, duresc, noord)
                context["message"] = "Escale updated successfully!"
            else:
                context["message"] = "IDESC is required to update an escale."

    context["escales"] = Escale.get_all_escale()

    return render_template("escale.html", context=context)