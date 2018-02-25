from wtforms import Form, validators, TextField

class RegistrationForm(Form): 
    username = TextField('username', [validators.required()])
    email = TextField('email')
    password = TextField('password')