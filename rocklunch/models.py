from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Sequence, SmallInteger
from . import engine

BaseModel = declarative_base()

class Company(BaseModel):

    __tablename__ = 'company'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64), unique = True)
    country = Column(String(32), unique = True)
    logo = Column(String(128), unique = True)

    def __repr__(self):
        return '<{} ({})>'.format(self.company, self.country)


class Vehicle(BaseModel):

    __tablename__ = 'vehicle'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle = Column(String(64), unique = True)
    modification = Column(String(32), unique = True)
    manufacturer = Column(Integer, ForeignKey("company.id"))
    logo = Column(String(128), unique = True)
    manufacturer = relationship("Company")

    def __repr__(self):
        return '<{} ({})>'.format(self.vehicle, self.modification)


class Satellite(BaseModel):

    __tablename__ = 'satellite'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    satellite = Column(String(64), unique = True)
    modification = Column(String(32), unique = True)
    manufacturer = Column(Integer, ForeignKey("company.id"))
    owner = Column(Integer, ForeignKey("company.id"))

    manufacturer = relationship("Company")
    owner = relationship("Company")

    def __repr__(self):
        return '<{} ({})>'.format(self.vehicle, self.modification)


class Spaceport(BaseModel):

    __tablename__ = 'spaceport'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    spaceport = Column(String(64), unique = True)
    complex = Column(String(64), unique = True)
    country = Column(String(32), unique = True)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return '<{} ({})>'.format(self.company, self.country)


BaseModel.metadata.create_all(engine)
