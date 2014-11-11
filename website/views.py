__author__ = 'thedoctor'
import sys
sys.path.append('../')
import os
from flask import render_template, url_for,request, redirect, send_from_directory
from website import app
from werkzeug.utils import secure_filename
from wav_plotter.main import Main


app.config['UPLOAD_FOLDER'] = ()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['.wav'])


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if app.config['ALLOWED_EXTENSIONS'] in file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                filename=filename))

    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
