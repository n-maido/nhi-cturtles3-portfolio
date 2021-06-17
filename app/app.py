from flask import Flask, render_template, url_for, request, redirect, json
import os
import json

app = Flask(__name__)
data_file = open('./static/data.json')
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



if __name__ == "__main__":
    # rid (port="5002") within run function
    app.run(debug=True) 
