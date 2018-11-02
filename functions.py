import requests #temp
from datetime import datetime

from database import session
from models import *

def db_add_agency(update):
    agency = session.query(Agency).get(update['id'])
    if not agency:
        agency = Agency()
    agency.id = update['id']
    agency.name = update['name']
    agency.abbrev = update['abbrev']
    agency.countryCode = update['countryCode']
    agency.type = update['type']
    agency.wikiURL = update['wikiURL']
    agency.changed = datetime.strptime(update['changed'], '%Y-%m-%d %H:%M:%S')
    agency.infoURLs = ','.join(update['infoURLs'])
    session.add(agency)
    session.commit()

def db_add_payload(update, mission_id):
    payload = session.query(Payload).get(update['id'])
    if not payload:
        payload = Payload()
    payload.id = update['id']
    payload.name = update['name']
    payload.mission_id = mission_id
    session.add(payload)
    session.commit()

def db_add_mission(update, launch_id):
    mission = session.query(Mission).get(update['id'])
    if not mission:
        mission = Mission()
    mission.id = update['id']
    mission.name = update['name']
    mission.description = update['description']
    mission.type = update['type']
    mission.wikiURL = update['wikiURL']
    mission.typeName = update['typeName']
    print(update)
    if update['agencies'] and len(update['agencies']) > 0:
        mission.agencies_id = update['agencies'][0]['id']
        db_add_agency(update['agencies'][0])
    for payload in update['payloads']:
        db_add_payload(payload, update['id'])
    mission.launch_id = launch_id
    session.add(mission)
    session.commit()

def db_add_rocket(update):
    rocket = session.query(Rocket).get(update['id'])
    if not rocket:
        rocket = Rocket()
    rocket.id = update['id']
    rocket.name = update['name']
    rocket.configuration = update['configuration']
    rocket.familyname = update['familyname']
    rocket.imageURL = update['imageURL']
    rocket.wikiURL = update['wikiURL']
    rocket.infoURLs	= ','.join(update['infoURLs'])
    if update['agencies'] and len(update['agencies']) > 0:
        rocket.agencies_id = update['agencies'][0]['id']
        db_add_agency(update['agencies'][0])
    session.add(rocket)
    session.commit()

def db_add_pads(update, location_id):
    pad = session.query(Pad).get(update['id'])
    if not pad:
        pad = Pad()
    pad.id = update['id']
    pad.name = update['name']
    pad.wikiURL = update['wikiURL']
    pad.mapURL = update['mapURL']
    pad.latitude = update['latitude']
    pad.longitude = update['longitude']
    if update['agencies'] and len(update['agencies']) > 0:
        pad.agencies_id = update['agencies'][0]['id']
        db_add_agency(update['agencies'][0])
    pad.location_id = location_id
    session.add(pad)
    session.commit()

def db_add_location(update):
    location = session.query(Location).get(update['id'])
    if not location:
        location = Location()
    location.id = update['id']
    location.name = update['name']
    location.wikiURL = update['wikiURL']
    location.countryCode = update['countryCode']
    for pad in update['pads']:
        db_add_pads(pad, update['id'])
    session.add(location)
    session.commit()

def db_add_launch(update):
    # Gets dictionary with launch info
    launch = session.query(Launch).get(update['id'])
    if not launch:
        launch = Launch()
    launch.id = update['id']
    launch.name = update['name']
    launch.windowstart = datetime.strptime(update['windowstart'], '%B %d, %Y %H:%M:%S %Z')
    launch.windowend = datetime.strptime(update['windowend'], '%B %d, %Y %H:%M:%S %Z')
    launch.net = datetime.strptime(update['net'], '%B %d, %Y %H:%M:%S %Z')
    launch.status = update['status']
    launch.inhold = update['inhold']
    launch.tbdtime = update['tbdtime']
    launch.vidURLs = ','.join(update['vidURLs'])
    launch.infoURLs = ','.join(update['infoURLs'])
    launch.holdreason = update['holdreason']
    launch.failreason = update['failreason']
    launch.tbddate = update['tbddate']
    launch.probability = update['probability']
    launch.hashtag = update['hashtag']
    launch.changed = datetime.strptime(update['changed'], '%Y-%m-%d %H:%M:%S')

    launch.lsp_id = update['lsp']['id']
    db_add_agency(update['lsp'])

    launch.rocket_id = update['rocket']['id']
    db_add_rocket(update['rocket'])

    launch.location_id = update['location']['id']
    db_add_location(update['location'])
    for mission in update['missions']:
        db_add_mission(mission, update['id'])

    session.add(launch)
    session.commit()


# Temporary
link = 'https://launchlibrary.net/1.4/launch/next/5'
data = requests.get(link).json()
launches = data['launches']
for l in launches:
    db_add_launch(l)

