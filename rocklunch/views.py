 # -*- coding: utf-8 -*-

from flask import request, render_template, url_for
from . import app
from .forms import *

import requests
import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    limit = request.args.get('limit', default = 10, type = int)
    startdate = request.args.get('startdate', default = '1961-04-12', type = str)
    enddate = request.args.get('enddate', default = datetime.date.today().isoformat(), type = str)

    link = 'https://launchlibrary.net/1.4/launch'
    params = {'startdate': startdate, 'enddate': enddate, 'limit': limit}
    data = requests.get(link, params = params).json()

    form = LaunchSearchForm(limit=limit, startdate=startdate, enddate=enddate)
    return render_template('all.html', form=form, launches=data['launches'], total=data['total'], count=data['count'])


@app.route('/upcoming')
def upcoming():
    link = 'https://launchlibrary.net/1.4/launch'
    limit = request.args.get('limit', default = 10, type = int)
    params = {'startdate': datetime.date.today(), 'limit': limit}
    data = requests.get(link, params = params).json()
    return render_template('upcoming.html', launches=data['launches'], total=data['total'], count=data['count'])


@app.route('/launch/<int:id>')
def launch(id):
    r = requests.get('https://launchlibrary.net/1.4/launch/' + str(id))
    launch = r.json()['launches'][0]
    return render_template('launch.html', launch=launch)

















