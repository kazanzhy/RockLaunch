from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine - the core interface to the database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create base class for mapping other models
BaseModel = declarative_base()

class Launch(BaseModel):
    '''
    Model for table of all launches
    '''
    __tablename__ = 'launch'

    id = Column(Integer, primary_key=True)
    code = Column(String(16), index = True, unique = True)
    link = Column(String(128), index = True, unique = True)
    redirects = Column(Integer)

    def __repr__(self):
        return '<Link ({}, {})>'.format(self.code, self.link)


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
