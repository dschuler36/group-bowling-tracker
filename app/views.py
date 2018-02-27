from flask import render_template
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask_login import login_user, logout_user, current_user, login_required
from passlib.hash import sha256_crypt
import sqlite3
import os
import gc
from .forms import RegistrationForm, LoginForm
from .models import User
from app import app, db


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login/", methods=["GET","POST"])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        # Log in the user
        flash('Logged in successfully!')
        return redirect(url_for('index'))

    return render_template("login.html")
