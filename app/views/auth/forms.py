from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
  email = EmailField(
    "Email Address",
    validators=[DataRequired("Forgot your email address?")]
    )
  password = PasswordField(
    "Password",
    validators=[DataRequired("Must provide a password. ;-)")]
    )

class RegisterForm(FlaskForm):
  email = EmailField(
    "Email Address",
    validators=[DataRequired("Write email address.")]
    )
  password = PasswordField(
    "Password",
    validators=[DataRequired("write password."), EqualTo("re_password","Not matehd password.")]
    )
  re_password = PasswordField(
    "RE-Password",
    validators=[DataRequired("Check password.")]
    )
  name = StringField(
    "Username",
    validators=[DataRequired("Write user name.")]
    )
  role = StringField(

  )