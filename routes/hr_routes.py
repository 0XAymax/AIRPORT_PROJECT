from flask import Blueprint, render_template, request, redirect, url_for
from models.emloyee  import Employee

# Create a blueprint
hr_routes = Blueprint('hr_routes', __name__)

@hr_routes.route("/hr", methods=["GET", "POST"])
def hr():
    print("HR route accessed")
    action = request.args.get("action", "list")  # Default action is "list"
    employee_id = request.args.get("id", type=int)  # Get the employee ID if provided
    search_name = request.form.get("search_name", "")  # Get the search name from the form
    search_fonction = request.form.get("search_fonction", "")  # Get the selected function
    min_salary = request.form.get("min_salary", type=float)  # Get the minimum salary
    max_salary = request.form.get("max_salary", type=float)  # Get the maximum salary
    start_date = request.form.get("start_date")  # Get the start date
    end_date = request.form.get("end_date")  # Get the end date
    context = {}  # Initialize context to pass data to the template

    # Handle each action
    if action == "list":
        context["employees"] = Employee.get_all()  # Fetch all employees
        context["view"] = "list"

    elif action == "search":
        context["employees"] = Employee.search_by_filters(search_name, search_fonction, min_salary, max_salary, start_date, end_date)
        context["view"] = "search"
        context["search_name"] = search_name
        context["search_fonction"] = search_fonction
        context["min_salary"] = min_salary
        context["max_salary"] = max_salary
        context["start_date"] = start_date
        context["end_date"] = end_date

    # ... (rest of your existing route logic remains the same)

    elif action == "details" and employee_id:
        context["employee"] = Employee.get_by_id(employee_id)  # Fetch employee by ID
        context["view"] = "details"

    elif action == "create":
        context["view"] = "create"
        if request.method == "POST":
            # Collect form data
            email = request.form.get("email")
            password = request.form.get("password")
            nom = request.form.get("NOM")
            prenom = request.form.get("prenom")
            tel = request.form.get("tel")
            ville = request.form.get("ville")
            adresse = request.form.get("adresse")
            salaire = request.form.get("salaire")
            fonction = request.form.get("FONCTION")
            datemb = request.form.get("datemb")

            # Validate fields
            if not all([email, password, nom, prenom, tel, ville, adresse, salaire, fonction, datemb]):
                context["error"] = "All fields are required!"
                return render_template("hr.html", context=context)

            # Create employee
            Employee.create(email, password, nom, prenom, tel, ville, adresse, float(salaire), fonction, datemb)
            return redirect(url_for('hr_routes.hr', action='list'))

    elif action == "update" and employee_id:
        context["employee"] = Employee.get_by_id(employee_id)  # Fetch employee by ID
        context["view"] = "update"
        if request.method == "POST":
            # Collect form data
            nom = request.form.get("NOM")
            prenom = request.form.get("prenom")
            email = request.form.get("email")
            tel = request.form.get("tel")
            adresse = request.form.get("adresse")
            salaire = request.form.get("salaire")
            ville = request.form.get("ville")
            fonction = request.form.get("FONCTION")

            # Update employee details
            Employee.set_full_name(employee_id, nom, prenom)
            Employee.set_email(employee_id, email)
            Employee.set_phone(employee_id, tel)
            Employee.set_address(employee_id, adresse)
            Employee.set_salary(employee_id, float(salaire))
            Employee.set_city(employee_id, ville)
            Employee.set_function(employee_id, fonction)
            return redirect(url_for('hr_routes.hr', action='details', id=employee_id))

    elif action == "delete" and employee_id and request.method == "POST":
        Employee.delete(employee_id)  # Delete employee
        return redirect(url_for('hr_routes.hr', action='list'))
    print(context)  # Debugging the context
    return render_template('hr.html', **context)  # Render the template with context
