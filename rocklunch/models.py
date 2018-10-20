from flask import url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import engine

BaseModel = declarative_base()

class Company(BaseModel):

    __tablename__ = 'company'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64))
    country = Column(String(32))
    logo = Column(String(128))

    vehicle = relationship("Vehicle", back_populates="company")
    satellite = relationship("Satellite", back_populates="company")

    def __repr__(self):
        return '{} ({})'.format(self.company, self.country)


class Vehicle(BaseModel):

    __tablename__ = 'vehicle'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle = Column(String(64))
    modification = Column(String(32))
    company_id = Column(Integer, ForeignKey("company.id"))
    logo = Column(String(128))

    company = relationship("Company", back_populates="vehicle")
    launch = relationship("Launch", back_populates="vehicle")

    def __repr__(self):
        return '{} ({})'.format(self.vehicle, self.modification)


class Satellite(BaseModel):

    __tablename__ = 'satellite'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    satellite = Column(String(64))
    modification = Column(String(32))
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="satellite")
    launch = relationship("Launch", back_populates="satellite")

    def __repr__(self):
        return '{} ({})'.format(self.vehicle, self.modification)


class Spaceport(BaseModel):

    __tablename__ = 'spaceport'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    spaceport = Column(String(64))
    complex = Column(String(64))
    country = Column(String(32))
    latitude = Column(Float)
    longitude = Column(Float)

    launch = relationship("Launch", back_populates="spaceport")

    def __repr__(self):
        return '{} ({})'.format(self.spaceport, self.complex)

class Launch(BaseModel):

    __tablename__ = 'launch'

    def __init__(self):
        pass

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    spaceport_id = Column(Integer, ForeignKey("spaceport.id"))
    satellite_id = Column(Integer, ForeignKey("satellite.id"))
    mission = Column(String(64))
    orbit = Column(String(16))
    webcast = Column(String(64))
    description = Column(String(512))
    window_from = Column(DateTime)
    window_start = Column(DateTime)
    window_to = Column(DateTime)

    satellite = relationship("Satellite", back_populates="launch")
    vehicle = relationship("Vehicle", back_populates="launch")
    spaceport = relationship("Spaceport",  back_populates="launch")

    def __repr__(self):
        return '{} ({})'.format(self.mission, self.vehicle)

    def get_url():
        return url_for('launch', args=[self.id])

BaseModel.metadata.create_all(engine)
















