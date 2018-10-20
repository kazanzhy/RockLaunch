 # -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, abort
from . import app, session
from .models import *
from .forms import *


@app.route('/admin')
def admin():
    abort(401)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/launches')
def launches():
    launches = []
    return render_template('launches.html', launches=launches)


@app.route('/spaceports')
def spaceports():
    ports = session.query(Spaceport).all()
    print(ports)
    return render_template('spaceports.html', ports=ports)


@app.route('/vehicles')
def vehicles():
    vehicles = []
    return render_template('vehicles.html', vehicles=vehicles)


@app.route('/companies')
def companies():
    companies = []
    return render_template('companies.html', companies=companies)








