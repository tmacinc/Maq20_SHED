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

@app.route('/_update_page_data') #Accepts requested variables when page is loaded and sends current values to page. Could also be used to keep track of what is needed in the back end.
def permeation_initialize():
    channels = []
    channels_requested = list(request.args.to_dict().keys())
    for channel in channels_requested:
        if channel in daq.channel_map:
            channels.append(channel)
        else:
            pass
    print(channels)
    data = daq.read_channels(channels)
    print(data)
    return jsonify(ajax_data=data)

@app.route('/_ffffffupdate_page_data')
def update_page_data():
    print(active_variables)

@app.route('/_maq20_fetch_data')
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    print(data)
    return jsonify(ajax_data=data)