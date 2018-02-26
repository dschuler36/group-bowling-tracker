from wtforms import Form, validators, TextField, PasswordField

class RegistrationForm(Form): 
    username = TextField('Username', [validators.required()])
    email = TextField('Email')
    password = PasswordField('Password')