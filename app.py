demo = True   # bool
if demo:
    import daq_demo as daq
else:
     import daq

from flask import Flask, render_template, jsonify, request
from threading import Thread, Event, Lock
from queue import Queue, Empty
from flask_socketio import SocketIO, emit
import json
from time import sleep
from datetime import datetime, timedelta
#import eventlet
from waitress import serve
import auxiliary_calculations

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#----------------- Load settings from config file ---------------------------------------------------------------------

with open('config.json') as json_file:
    settings = json.load(json_file)
#socketio = SocketIO(app)
daq = daq.dataforth(settings)


#----------------- Build variables dictionary - Can also have scales, eng units etc -----------------------------------
## convert this to class once finalized?

variables = {}
variables["daq_channels"] = []
variables["vars_raw"] = {}
variables["vars_eng"] = {}
for key in settings["channel_map_inputs"]:
    variables['daq_channels'].append(key)
for key in settings["channel_map_outputs"]:
    variables['daq_channels'].append(key)
for channel in variables['daq_channels']:
    variables["vars_raw"][channel] = 0
for channel in variables['daq_channels']:
    variables['vars_eng'][channel] = 0
variables['vars_eng']['T_shed2'] = 12.34
variables['vars_eng']['T_shed3'] = 12.34
calibration = settings["calibration"]




#------------------- Route Functions - Perform task when browser directs to link (serve html etc) ---------------------

@app.route('/')
def index():
    return render_template('permeation.html')

@app.route('/maq20_overview.html')
def maq20_overview():
    return render_template('maq20_overview.html')

@app.route('/permeation.html')
def permeation():
    return render_template('permeation.html')

@app.route('/_update_page_data') #Accepts requested variables when page is loaded and sends current values to page. Could also be used to keep track of what is needed in the back end.
def update_page_data():
    channels_requested = list(request.args.to_dict().keys())
    data = {}
    for channel in channels_requested:
        if channel in variables['vars_eng'].keys():
            data[channel] = variables['vars_eng'][channel]

    return jsonify(ajax_data=data)

@app.route('/_set_control') #Accepts requested control variable from user and sends value to controller.
def set_control():
    msg = request.args.to_dict()
    channels = list(request.args.to_dict().keys())
    channel_name = channels[0]
    print("Received request to update setting: " + channel_name + " to new value: " + msg[channel_name])
    queue.put({"write_channels": msg})
    return jsonify(ajax_response="Received channel -> value: " + str(channel_name) + " -> " + str(msg[channel_name]))

@app.route('/_maq20_fetch_data') #Used for maq20_overview.html
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    return jsonify(ajax_data=data)

#--------------------- Regular functions - Can be used by routes, background thread etc. ------------------------------

def read_daq(): # get current channel values from list in variables['vars_raw']
    channels = variables['daq_channels']
    data = daq.read_channels(channels)
    update_variables(data)

def update_variables(data): # updates the variables dictionary with new values
    for key in data.keys():
        variables['vars_raw'][key] = data[key]
    variables['vars_eng'] = auxiliary_calculations.raw_to_eng(variables['vars_raw'])

def background_tasks(queue=Queue): # Parallel function to the Flask functions. Used for managing daq, control functions etc. Will run without client connected.
    print("Background thread started")
    t_now = datetime.now()
    t_next = t_now + timedelta(seconds=1)
    while True:
        while t_now < t_next:                               # runs at higher frequency
            if not queue.empty(): # process queue
                task = queue.get()
                for key in task.keys():
                    if key == "write_channels":
                        daq.write_channels(task[key])
            t_now = datetime.now()
            sleep(0.01)
        t_next = t_next + timedelta(seconds=1)              # runs every 1 second
        t_now = datetime.now()
        read_daq()


#--------------------- Initialize background thread and start flask app ------------------------------------------------


queue = Queue()
background = Thread(target=background_tasks, args=(queue,))
background.daemon = True
background.start()


if __name__ == '__main__':
    #socketio.run(app, host='0.0.0.0')  # used for eventlet with socketio
    serve(app, port=5000)               # used for waitress, without sockets