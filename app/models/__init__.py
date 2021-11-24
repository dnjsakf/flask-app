from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):
  __abstract__  = True

  reg_date = db.Column(db.DateTime,  default=db.func.current_timestamp())
  upd_date = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                     onupdate=db.func.current_timestamp())

# Import Models
from app.models.users import *