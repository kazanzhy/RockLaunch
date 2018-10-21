 # -*- coding: utf-8 -*-

from flask import Flask

# Application
app = Flask(__name__)
app.config.from_object('config')

from rocklunch import views
