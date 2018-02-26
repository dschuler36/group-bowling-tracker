from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
# app.config.from_object('config')
app.secret_key = os.urandom(24)
Bootstrap(app)


from app import views
