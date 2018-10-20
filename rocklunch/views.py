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
    launches = session.query(Launch).all()
    return render_template('launches.html', launches=launches)


@app.route('/spaceports')
def spaceports():
    ports = session.query(Spaceport).all()
    return render_template('spaceports.html', ports=ports)


@app.route('/vehicles')
def vehicles():
    vehicles = session.query(Vehicle).all()
    return render_template('vehicles.html', vehicles=vehicles)


@app.route('/companies')
def companies():
    companies = session.query(Company).all()
    return render_template('companies.html', companies=companies)


@app.route('/add')
def add():
    form = []
    return render_template('add.html', form=form)

















