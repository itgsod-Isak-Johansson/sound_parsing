__author__ = 'thedoctor'
from flask import Flask
app = Flask(__name__)

import os


app.config['ALLOWED_EXTENSIONS'] = set(['wav'])
thisfile = os.path.abspath(__file__)
soundfiles = os.path.join(os.path.dirname(thisfile), 'static/soundfiles')
uploads = os.path.join(os.path.dirname(thisfile), 'static/tmp.Cra8lk4Uyb')
plots = os.path.join(os.path.dirname(thisfile), 'static/plots')
app.config['SOUND_FILES'] = soundfiles
app.config['UPLOAD_FOLDER'] = uploads
app.config['PLOTS'] = plots


import views