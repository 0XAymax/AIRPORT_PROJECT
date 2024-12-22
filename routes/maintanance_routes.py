from flask import Blueprint, render_template, request, redirect, url_for, flash
from AIRPORT_PROJECT.models.revision import Revision
from AIRPORT_PROJECT.models.aircraft import Aircraft
from AIRPORT_PROJECT.models.emloyee import Employee
from datetime import datetime

maintanance_routes = Blueprint('maintanance_routes', __name__)

@maintanance_routes.route('/maintanance', methods=["GET", "POST"])

def maintenance():
    context = {}
    action = request.args.get("action", "list")
    aircraft_id = request.args.get("id", type=int)
    tech_name = request.form.get("tech_name")
    tech_id = request.form.get("tech_id", type=int)

    try:
        if action == "list":
            # Get all aircraft needing maintenance
            context["aircrafts"] = Aircraft.get_by_status('ReqMaintenance')
            context["view"] = "list"

        elif action == "revision_form" and aircraft_id:
            if request.method == "POST":
                # Validate form data
                rapport = request.form.get("rapport")
                daterev = request.form.get("daterev")
                tecid = request.form.get("tecid")
                new_status = request.form.get("new_status")

                if not all([rapport, daterev, tecid, new_status]):
                    flash("All fields are required", "error")
                    return redirect(request.url)

                try:
                    # Create revision and update aircraft status
                    Revision.create_revision(rapport, daterev, aircraft_id, tecid)
                    Aircraft.update_aircraft(aircraft_id, status=new_status)
                    flash("Revision created successfully", "success")
                    return redirect(url_for('maintanance_routes.maintenance'))
                except Exception as e:
                    flash(f"Error creating revision: {str(e)}", "error")
                    return redirect(request.url)

            # Get data for the form
            context["aircraft"] = Aircraft.get_by_id(aircraft_id)
            context["previous_revisions"] = Revision.get_revisions_by_aircraft(aircraft_id)
            context["technicians"] = Employee.search_employees(fonction="Technician")
            context["view"] = "revision_form"

        elif action == "search_revisions":
            if request.method == "POST":
                # Search revisions by technician
                revisions = Revision.search_technician_revisions(tech_name, tech_id)
                context["revisions"] = revisions
                context["search_name"] = tech_name
                context["search_id"] = tech_id
            context["view"] = "search_revisions"

        elif action == "revision_details":
            revision_id = request.args.get("revision_id", type=int)
            if not revision_id:
                flash("Revision ID is required", "error")
                return redirect(url_for('maintanance_routes.maintenance'))

            revision = Revision.get_revision_by_id(revision_id)
            if not revision:
                flash("Revision not found", "error")
                return redirect(url_for('maintanance_routes.maintenance'))

            context["revision"] = revision
            context["view"] = "revision_details"

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('maintanance_routes.maintenance'))

    context["statuses"] = ["Available", "OutOfService", "ReqMaintenance"]
    return render_template('maintanance.html', **context)
