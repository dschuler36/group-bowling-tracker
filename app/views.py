from flask import render_template
from app import app

@app.route('/')
def homepage():
    return ("hello bowling world")