from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import os

app = Flask(__name__)
# app.config.from_object('config')
app.secret_key = os.urandom(24)
Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

from app import views
