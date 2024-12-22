from flask import Flask,render_template,url_for
from routes.auth import auth_blueprint 
from routes.aircraft_routes import aircraft_routes
from routes.airport_routes import airport_routes
from routes.escale_routes import escale_routes
from routes.flight_routes import flight_routes
from routes.crew_routes import crew_routes
from routes.maintanance_routes import maintanance_routes
from routes.hr_routes import hr_routes
from routes.nav_staff_routes import nav_staff_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

app.register_blueprint(auth_blueprint)
app.register_blueprint(aircraft_routes)
app.register_blueprint(airport_routes)
app.register_blueprint(escale_routes)
app.register_blueprint(flight_routes)
app.register_blueprint(crew_routes)
app.register_blueprint(maintanance_routes)
app.register_blueprint(hr_routes)
app.register_blueprint(nav_staff_routes)



if __name__ == '__main__':
    app.run(debug=True)
