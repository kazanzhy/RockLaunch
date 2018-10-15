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
    return "Hello, World!"
