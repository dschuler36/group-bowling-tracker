from flask import render_template
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import sqlite3
import os
# from MySQLdb import escape_string as thwart
import gc
from .forms import RegistrationForm
from app import app

def db_conn():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    db_path = os.path.join(BASE_DIR, "..", "sql\\bowling.db")
    print(db_path)
    conn = sqlite3.connect(db_path) 
    return c, conn


@app.route('/')
def home_page():
    return render_template('homepage.html')


@app.route('/register/', methods=["GET","POST"])
def register_page():
    print("hello form")
    try:
        form = RegistrationForm(request.form) 
        print(form.username.data)

        if request.method == "POST" and form.validate():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = db_conn()

            x = c.execute("SELECT * FROM users WHERE username = '?'", username)

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                          (thwart(username), thwart(password), thwart(email)))
                
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))

@app.route("/login/", methods=["GET","POST"])
def login_page(): 
    return render_template("login.html")