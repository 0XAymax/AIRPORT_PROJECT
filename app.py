from flask import Flask
from routes.auth import auth_blueprint 

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Register the blueprint
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
