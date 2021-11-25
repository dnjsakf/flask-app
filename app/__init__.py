import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

# Initialize Flask App
app = Flask(
    __name__
    , template_folder="templates"
    , static_url_path="/public/"
    , static_folder="static"
)

# Configurations
app.config.from_object("app.config.Development")

# Initialize Database
db = SQLAlchemy(app)
db.create_all()

# Error Handler: Not Found
@app.errorhandler(404)
def not_found(error):
  return ( render_template('404.html', error=error), 404 )
    
@app.context_processor
def override_url_for():
  return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
  if endpoint == "static":
    filename = values.get('filename', None)
    if filename:
      values['q'] = int(os.stat(os.path.join(app.static_folder, filename)).st_mtime)
  return url_for(endpoint, **values)

# Register Blueprints
from app.views import view as view_index
from app.views.auth import view as view_auth
app.register_blueprint(view_index)  # url_prefix="/"
app.register_blueprint(view_auth)  # url_prefix="/auth"

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

from app.gql import schema
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)