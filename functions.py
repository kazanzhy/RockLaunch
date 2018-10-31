import requests
from datetime import datetime

from database import session
from models import *


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
    launch.wsstamp = update['wsstamp']
    launch.westamp = update['westamp']
    launch.netstamp = update['netstamp']
    launch.isostart = update['isostart']
    launch.isoend = update['isoend']
    launch.isonet = update['isonet']
    launch.status = update['status']
    launch.inhold = update['inhold']
    launch.tbdtime = update['tbdtime']
    launch.vidURLs = update['vidURLs']
    launch.vidURL = update['vidURL']
    launch.infoURLs = update['infoURLs']
    launch.infoURL = update['infoURL']
    launch.holdreason = update['holdreason']
    launch.failreason = update['failreason']
    launch.tbddate = update['tbddate']
    launch.probability = update['probability']
    launch.hashtag = update['hashtag']
    launch.changed = datetime.strptime(update['changed'], '%Y-%m-%d %H:%M:%S')
    session.add(launch)
    session.commit()


# Temporary
link = 'https://launchlibrary.net/1.4/launch/next/5'
data = requests.get(link).json()
launches = data['launches']
for l in launches:
    db_add_launch(l)

