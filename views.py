from flask import render_template
from app import app
from schedule_api import get_terms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meetlafamilia')
def lafamilia():
    return render_template('meetlafamilia.html')


@app.route('/PV2013')
def pv():
    return render_template('PV2013.html')

@app.route('/PC2014')
def pc():
    return render_template('PC2014.html')

