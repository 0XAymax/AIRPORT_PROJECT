from flask import Flask, render_template, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import datetime

from routes.aircraft_routes import aircraft_routes
from routes.airport_routes import airport_routes
from routes.hr_routes import hr_routes
from routes.maintanance_routes import maintanance_routes

app = Flask(__name__)

# Register template filter for current year
@app.template_filter('current_year')
def current_year_filter(text):
    return datetime.now().year

# Register blueprints
app.register_blueprint(aircraft_routes)
app.register_blueprint(airport_routes)
app.register_blueprint(hr_routes)
app.register_blueprint(maintanance_routes)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
