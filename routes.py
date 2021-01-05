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
def update_page_data():
#    channels = []
    channels_requested = list(request.args.to_dict().keys())
#    for channel in channels_requested:
    #    if channel in daq.channel_map:
#        channels.append(channel)
    #    else:
    #        pass
#    print(channels_requested)
    data = daq.read_channels(channels_requested)
    print(data)
    return jsonify(ajax_data=data)

@app.route('/_set_control') #Accepts requested control variable from user and sends value to controller.
def set_control():
    msg = request.args.to_dict()
#    print(msg)
    channels = list(request.args.to_dict().keys())
    channel_name = channels[0]
    print("Received request to update setting: " + channel_name + " to new value: " + msg[channel_name])
    daq.write_channels(msg)
    return jsonify(ajax_response="Received channel -> value: " + str(channel_name) + " -> " + str(msg[channel_name]))

@app.route('/_maq20_fetch_data')
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    print(data)
    return jsonify(ajax_data=data)