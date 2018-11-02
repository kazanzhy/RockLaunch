from sqlalchemy import Column, ForeignKey, SmallInteger, Integer, BigInteger, Float, String, DateTime, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import engine

# Create base class for mapping other models
BaseModel = declarative_base()

class Chat(BaseModel):
    # Model for table of all bot dialogs
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    username = Column(String(32))
    def __repr__(self):
        return '{} {} (@{})'.format(self.first_name, self.last_name, self.username)

class Agency(BaseModel):
    # Model for table of all agencies and launch service providers
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    abbrev = Column(String(16))
    countryCode = Column(String(16))
    type = Column(SmallInteger)
    wikiURL = Column(String(256))
    changed	= Column(DateTime(timezone=True))
    infoURLs = Column(String(1024))
    def __repr__(self):
        return '{}'.format(self.name)

class Pad(BaseModel):
    # Model for table of launch pads
    __tablename__ = 'pad'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    wikiURL = Column(String(256))
    mapURL = Column(String(256))
    latitude = Column(Float)
    longitude = Column(Float)
    agencies_id = Column(Integer, ForeignKey('agency.id'))
    agencies = relationship('Agency')
    location_id = Column(Integer, ForeignKey('location.id'))
    def __repr__(self):
        return '{}'.format(self.name)

class Location(BaseModel):
    # Model for table of all locations
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    infoURL = Column(String(256))
    wikiURL = Column(String(256))
    countryCode = Column(String(16))
    pads = relationship('Pad')
    def __repr__(self):
        return '{}'.format(self.name)

class Rocket(BaseModel):
    # Model for table of all rockets
    __tablename__ = 'rocket'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    configuration = Column(String(16))
    familyname = Column(String(64))
    agencies_id = Column(Integer, ForeignKey('agency.id'))
    agencies = relationship('Agency')
    wikiURL = Column(String(256))
    imageURL = Column(String(256))
    infoURLs = Column(String(1024))
    def __repr__(self):
        return '{}'.format(self.name)

class Payload(BaseModel):
    # Model for table of all payloads
    __tablename__ = 'payload'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    mission_id = Column(Integer, ForeignKey('mission.id'))
    def __repr__(self):
        return '{}'.format(self.name)

class Mission(BaseModel):
    # Model for table of all missions
    __tablename__ = 'mission'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(1024))
    type = Column(SmallInteger)
    wikiURL = Column(String(256))
    typeName = Column(String(64))
    agencies_id = Column(Integer, ForeignKey('agency.id'))
    agencies = relationship('Agency')
    payloads = relationship('Payload')
    launch_id = Column(Integer, ForeignKey('launch.id'))
    def __repr__(self):
        return '{}'.format(self.name)

class Launch(BaseModel):
    # Model for table of all launches
    __tablename__ = 'launch'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    windowstart	= Column(DateTime(timezone=True))
    windowend	= Column(DateTime(timezone=True))
    net	= Column(DateTime(timezone=True))
    status = Column(SmallInteger)
    inhold = Column(SmallInteger)
    tbdtime = Column(SmallInteger)
    vidURLs = Column(String(1024))
    infoURLs = Column(String(1024))
    holdreason = Column(String(64))
    failreason = Column(String(64))
    tbddate	= Column(SmallInteger)
    probability	= Column(SmallInteger)
    hashtag	= Column(String(64))
    changed	= Column(DateTime(timezone=True))
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship('Location')
    rocket_id = Column(Integer, ForeignKey('rocket.id'))
    rocket = relationship('Rocket')
    missions = relationship('Mission')
    lsp_id = Column(Integer, ForeignKey('agency.id'))
    lsp = relationship("Agency")

    def __repr__(self):
        return '{}'.format(self.name)

BaseModel.metadata.create_all(engine)


