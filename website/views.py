__author__ = 'thedoctor'
import sys, os
sys.path.append('../')
from flask import render_template, url_for,request, redirect
from website import app
from wav_plotter.main import Main
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plots', methods=['GET','POST'])
def plots():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_plots', filename=filename))
        else:
            return 'not a valid file!'
    return render_template('plots.html')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/plots/<filename>')
def show_plots(filename):
    filename_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    filename = filename.replace('.wav', '.png')
    plot1 = 'time-amplitude-plot-{0}'.format(filename)
    plot2 = 'frequency-power-plot-{0}'.format(filename)
    main = Main(filename_path, os.path.join(app.config['PLOTS'], plot1), os.path.join(app.config['PLOTS'], plot2))
    main.class_manager()
    print plot1, plot2
    return render_template('show_plots.html', plot1='/static/plots/{0}'.format(plot1), plot2='/static/plots/{0}'.format(plot2))
