from wtforms import Form, validators, TextField, PasswordField

class RegistrationForm(Form): 
    username = TextField('Username', [validators.required()])
    email = TextField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(),])