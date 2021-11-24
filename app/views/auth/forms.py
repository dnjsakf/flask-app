from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
  email = EmailField(
    "Email Address",
    validators=[
        DataRequired("Forgot your email address?")
    ])
  password = PasswordField(
    "Password",
    validators=[
        DataRequired("Must provide a password. ;-)"),
        Length(min=4, max=16)
    ],
    description={
        "placeholder": "Write your email address."
    })

class RegisterForm(FlaskForm):
  email = EmailField(
    "Email Address",
    validators=[
        DataRequired("Email is required.")
    ])
  password = PasswordField(
    "Password",
    validators=[
        DataRequired("Password is required."),
        Length(min=4, max=16),
    ])
    
  re_password = PasswordField(
    "Re-Password",
    validators=[
        DataRequired("Re-Password is required."),
        EqualTo("password", "Not matehd password."),
        Length(min=4, max=16)
    ])
  name = StringField(
    "Username",
    validators=[
        DataRequired("Username is required."),
    ])
  role = StringField()