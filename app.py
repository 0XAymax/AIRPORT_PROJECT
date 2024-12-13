from flask import Flask,render_template,url_for
from routes.auth import auth_blueprint 
from routes.aircraft_routes import aircraft_routes
from routes.airport_routes import airport_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


app.register_blueprint(aircraft_routes)
app.register_blueprint(airport_routes)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
