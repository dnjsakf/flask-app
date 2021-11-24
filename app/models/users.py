from app import db
from app.models import Base

# Define a User model
class User(Base):
  __tablename__ = 'MT_USERS'

  # Identification Data: email & password
  email = db.Column(db.String(128), nullable=False, primary_key=True, unique=True)
  password = db.Column(db.String(192), nullable=False)

  # User Name
  name = db.Column(db.String(128), nullable=False)

  # Authorisation Data: role & status
  role = db.Column(db.SmallInteger, nullable=True)
  status = db.Column(db.SmallInteger, nullable=True)

  # New instance instantiation procedure
  def __init__(self, name, email, password):
    self.email = email
    self.password = password
    self.name = name

  def __repr__(self):
    return '<User %r>' % (self.name)
