import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):    
  # Application threads. A common general assumption is
  # using 2 per available processor cores - to handle
  # incoming requests using one and performing background
  # operations using the other.
  THREADS_PER_PAGE = 2

  # Enable protection agains *Cross-site Request Forgery (CSRF)*
  CSRF_ENABLED = True
  
  # Use a secure, unique and absolutely secret key for
  # signing the data. 
  CSRF_SESSION_KEY = "heo.dochi.dolf.flask.app.csrf.session.secret.key"

  # Secret key for signing cookies
  SECRET_KEY = "heo.dochi.dolf.flask.app.secret.key"

# Statement for enabling the development environment
class Development(Config):
  DEBUG = True

  # Define the database - we are working with
  # SQLite for this example
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
  DATABASE_CONNECT_OPTIONS = {}

# Statement for enabling the production environment
class Production(Config):
  DEBUG = False
