from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

# Create engine - the core interface to the database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create session for queries
Session = sessionmaker(bind=engine)
session = Session()
