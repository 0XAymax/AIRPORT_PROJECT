from flask import Flask, render_template
from login_form import loginform 
import os


app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'fallback_secret_key')  

@app.route("/", methods=["GET", "POST"])  
def login():
    form = loginform()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)

