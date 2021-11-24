import bcrypt

from flask import (
  Blueprint, render_template,
  flash, session, redirect, url_for
)

from app import db
from app.models import User
from app.views.auth.forms import LoginForm, RegisterForm

view = Blueprint("auth", __name__, url_prefix="/auth")

@view.route("/signin/", methods=["GET", "POST"])
def signin():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    
    if user and bcrypt.checkpw(form.password.data.encode("utf-8"), user.password.encode("utf-8")):
        session["user_id"] = user.email

        flash(user.name, "signin")

        return ( redirect(url_for("main.index")), 302 )

    else:
      flash("Wrong email or password", "error")

  return ( render_template("auth/signin.html", form=form), 200 )


@view.route("/signup/", methods=["GET", "POST"])
def signup():
  form = RegisterForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if not user:
      new_user = User(
        email = form.email.data,
        password = bcrypt.hashpw(form.password.data.encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        name = form.name.data
      )
      db.session.add(new_user)
      db.session.commit()
    
      return ( redirect(url_for("auth.signin")), 302 )

    else:
      flash("Already used email address, %s." % form.email.data, "error")

  return ( render_template("auth/signup.html", form=form), 200 )
