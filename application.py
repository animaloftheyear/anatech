import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///anatech.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/what")
def what():
    return render_template("what.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        # insert data:
        result = db.execute("INSERT INTO customers (name, email, phone, message) VALUES(:name, :email, :phone, :message)", name=request.form.get("name"), email=request.form.get("email"), phone=request.form.get("phone"), message=request.form.get("message"))
        return redirect("/contact")
    return render_template("contact.html")