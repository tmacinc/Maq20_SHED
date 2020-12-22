from app import app, daq
from flask import render_template, jsonify, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maq20_overview.html')
def maq20_overview():
    return render_template('maq20_overview.html')

@app.route('/permeation.html')
def permeation():
    return render_template('permeation.html')

@app.route('/_initialize_page_data') #make this bidirectional and accept IDs to initialize, can use for each page.
def permeation_initialize():
    #add data to initialize fields
    print(request.args.)
    channels = ['Pump_main_hot', 'Temp_main_hot', 'Valve_main_hot', 'Pump_main_cold', 'Temp_main_cold', 'Valve_main_cold']
    data = daq.read_channels(channels)
    return jsonify(ajax_data=data)

@app.route('/_maq20_fetch_data')
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    print(data)
    return jsonify(ajax_data=data)