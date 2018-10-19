 # -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, abort
from . import app#, session
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
    return render_template('launches.html')

@app.route('/spaceports')
def spaceports():
    return render_template('spaceports.html')

@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')
