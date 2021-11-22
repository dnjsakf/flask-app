from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

# Register Blueprints
from app.views import view as view_index
from app.views.auth import view as view_auth
app.register_blueprint(view_index)  # url_prefix="/"
app.register_blueprint(view_auth)  # url_prefix="/auth"

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
