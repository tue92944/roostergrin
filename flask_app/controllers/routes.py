from flask_app import app
from flask import render_template,request,redirect,session,flash

@app.route('/')
def home():
    return render_template("index.html")
