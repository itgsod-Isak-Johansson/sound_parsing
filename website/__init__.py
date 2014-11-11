__author__ = 'thedoctor'
from flask import Flask
app = Flask(__name__)

import os

thisfile = os.path.abspath(__file__)
soundfiles = os.path.join(os.path.dirname(thisfile), 'static/soundfiles')
uploads = os.path.join(os.path.dirname(thisfile), 'static/uploads')


import views