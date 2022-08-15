import re
from flask import Flask, redirect, url_for, render_template, request
from mariadbTestermariaCheck, import mariaCheck
import sys

app = Flask(__name__)

inp = ''

def type():
    global inp
    inp = input("What would you like the website to say?")
    return str(inp)

@app.route("/")
def home():
    if request.method == "POST":
        return redirect(url_for("login"))   
    else:
        return render_template("index.html", content='hi')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        if 
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return render_template("loginpasswd.html", user=usr) 


if __name__ == '__main__': 
    app.run(debug=True)

    This is where i decide that im going to make a sad tik 