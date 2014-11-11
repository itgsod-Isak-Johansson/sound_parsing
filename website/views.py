__author__ = 'thedoctor'
import sys, os
sys.path.append('../')
from flask import render_template, url_for,request, redirect
from website import app, soundfiles
from wav_plotter.main import Main


@app.route('/', methods=['GET', 'POST'])
def home():
    filename = 'a.wav'

    if request.method == 'POST':
        return redirect(url_for('plots', filename=filename))
    return render_template('index.html')


@app.route('/<filename>', methods=['GET', 'POST'])
def plots(filename):
    filename_path = os.path.join(soundfiles, filename)
    main = Main(filename_path, filename)
    plot1, plot2 =main.class_manager()
    return render_template('plots.html', plot1=plot1,  plot2=plot2)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
