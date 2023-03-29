from app import app

from flask import render_template

@app.route("/")
def login() :
    return render_template("login.html" , title = "LOG IN")

@app.route("/user")
def index() :
    return render_template("usermanager.html" , title = "User")

@app.route("/table")
def base() :
    return render_template("table.html" , title = "base")
