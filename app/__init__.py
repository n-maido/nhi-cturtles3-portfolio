from flask import Flask, render_template, url_for, request, redirect, json
import os
import json
from . import db

from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

app = Flask(__name__)

app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

data_file = open('./app/static/data.json')
data = json.load(data_file)
#data_file.close()



#Create URL routes
@app.route('/')
def home():
    allUsers = data
    return render_template("home.html", allUsers=allUsers)

#Create URL for each members
@app.route('/about/<string:name>')
def about(name):
    userData = data[name]
    allUsers = data
    return render_template("about.html", name=name, userData=userData, allUsers=allUsers)

@app.route('/health', methods=["GET"])
def health():
    return "<h1>Request received<h1>", 200

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        # validate that user details aren't empty and user isn't already registered
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None: #return 1 row
            error = f"User {username} is already registered."

        # store user details
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password)) # hash password and store hash instead of actual password
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return a register page
    return "Register Page not yet implemented", 501

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute( 
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # Validate details
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200 
        else:
            return error, 418
    
    ## TODO: Return a login page
    return "Login Page not yet implemented", 501


if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run(debug=True) 
