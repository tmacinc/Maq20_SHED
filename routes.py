from app import app, daq
from flask import render_template, jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maq20_overview.html')
def maq20_overview():
    return render_template('maq20_overview.html')

@app.route('/_maq20_fetch_data')
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    print(data)
    return jsonify(ajax_data=data)