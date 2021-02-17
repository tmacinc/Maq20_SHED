demo = False   # bool
if demo:
    import daq_demo as daq
else:
     import daq
from alarms import alarm
from flask import Flask, render_template, jsonify, request
from threading import Thread, Event, Lock
from queue import Queue, Empty
from flask_socketio import SocketIO, emit
import json
from time import sleep
from datetime import datetime, timedelta
from simple_pid import PID

#import eventlet                # If using sockets. Otherwise sockets will use long polling (cross platform)
from waitress import serve      # Production server for windows applications
#import gunicorn                # Production server for linux applications
import auxiliary_calculations


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
#socketio = SocketIO(app)       # If using sockets. Binds SocketIO to app

#----------------- Load settings from config file, initiate daq -------------------------------------------------------

with open('config.json') as json_file:
    settings = json.load(json_file)

#socketio = SocketIO(app)
daq = daq.dataforth(settings)


#----------------- Build variables dictionary - Can also have scales, eng units etc -----------------------------------
## convert this to class once finalized?

daq_channels = []
for key in settings["channel_map_inputs"]:
    daq_channels.append(key)
for key in settings["channel_map_outputs"]:
    daq_channels.append(key)
vars_raw = {}
for channel in daq_channels:
    vars_raw[channel] = 0
vars_eng = {}
for channel in vars_raw.keys():
    vars_eng[channel] = vars_raw[channel]
vars_sys = {}
for channel in settings['system_variables'].keys():
    vars_sys[channel] = settings['system_variables'][channel]
calibration = settings["calibration"]
#var_sys = {"SHED1": {"status": "off"}, "SHED2": {"status": "off"}, "SHED3": {"status": "off"}} ## parse in from JSON file

pid_SHED3 = PID(vars_sys["SHED3"]["PID"]["p"],vars_sys["SHED3"]["PID"]["i"], vars_sys["SHED3"]["PID"]["d"], vars_sys["SHED3"]["set_temp"])
pid_SHED3.output_limits =  (vars_sys["SHED3"]["PID"]["limits"]["low"],vars_sys["SHED3"]["PID"]["limits"]["high"])


def pid_control(pid, current_temp, set_temp):
    pid.setpoint = set_temp
    return pid(current_temp)

#------------------- Initialize alarms ---------------------------------------------------------------------------------

alarms = []
for key in settings['alarm']:
    alarms.append(alarm(key, settings['alarm'][key])) 

#------------------- Route Functions - Perform task when browser directs to link (serves html etc) ---------------------

#------------------- Html routes ---------------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('permeation.html')

@app.route('/maq20_overview.html')
def maq20_overview():
    return render_template('maq20_overview.html')

@app.route('/permeation.html')
def permeation():
    return render_template('permeation.html')

@app.route('/all_health.html')
def all_health():
    return render_template("all_health.html")

#------------------- Data routes used by JQuery ------------------------------------------------------------------------

@app.route('/_update_page_variables')                            #Accepts variables list from js and returns current values. 
def update_page_data():
    variables_requested = list(request.args.to_dict().keys())
    data = {}
    for variable in variables_requested:
        if variable in vars_eng.keys():
            data[variable] = vars_eng[variable]
    #print(variables_requested)
    return jsonify(ajax_data=data)

@app.route('/_set_variable_value')                                 #Accepts requested control variable from user and sends values to background task.
def set_variable_value():
    variable_to_set = request.args.to_dict()
    variable = list(request.args.to_dict().keys())
    variable_name = variable[0]
    print("Received request to update setting: " + variable_name + " to new value: " + variable_to_set[variable_name])
    queue.put({"write_channels": variable_to_set})
    return jsonify(ajax_response="Received variable -> value: " + str(variable_name) + " -> " + str(variable_to_set[variable_name]))

@app.route('/_maq20_fetch_data')                            #Used for maq20_overview.html - not super useful outside of an overview
def maq20_fetch_data():
    data = daq.read_modules(daq.modules)
    return jsonify(ajax_data=data)

#--------------------- Regular functions - Can be used by routes, background thread etc. --------------------------------------------------------

def read_daq():                                             # get current channel values from list in vars_raw
    channels = daq_channels
    data = daq.read_channels(channels)
    #print(data)
    update_daq_variables(data)

def update_daq_variables(data):                                 # updates the variables dictionary with new values
    for key in data.keys():
        vars_raw[key] = data[key]
    temp = auxiliary_calculations.raw_to_eng(vars_raw, calibration)
    for key in temp.keys():
        vars_eng[key] = temp[key]

def update_calculated_variables():
    vars_eng["T_shed2"] = round((vars_eng["T_shed2_l"] + vars_eng["T_shed2_r"] / 2), 2)
    vars_eng["T_shed3"] = round((vars_eng["T_shed3_l"] + vars_eng["T_shed3_r"] / 2), 2)

def update_remote_request():    
    if vars_raw["Request_shed1"] == 1:
        vars_sys["SHED1"]["request"] = "on"
    if vars_raw["Request_shed2"] == 1:
    #     vars_sys["SHED2"]["request"] = "on"
        pass
    if vars_raw["Request_shed3"] == 1:
        vars_sys["SHED3"]["request"] = "on"
 
def SHED_control(SHED):# Action when User Input toggles SHED(n) state
    """
    param: SHED(n) dictionary
    return: output_dict -> to be used in daq_write() function
    """
    output_dict = {}
    
    if vars_sys[SHED]['state'] == 0:
        vars_sys[SHED]['state'] = 1
        output_dict  = vars_sys[SHED]['active_config']
    elif vars_sys[SHED]['state'] == 1 or vars_sys[SHED]['state'] == 2:
        vars_sys[SHED]['state'] = 0
        output_dict = vars_sys[SHED]['inactive_config']
    else: # SHED_status == 3 ##> Alarm function RESET ALARM and turn all function off
        vars_sys[SHED]['state'] = 0
        output_dict = vars_sys[SHED]['inactive_config']  
    
    return output_dict

#--------------------- Background Task - This Parallel function to the Flask functions. Used for managing daq, calling threads with control functions etc. Will run without client connected.

def background_tasks(queue=Queue): 
    print("Background thread started")
    t_now = datetime.now()
    t_next = t_now + timedelta(seconds=1)
    while True:
        while t_now < t_next:                               # runs at higher frequency (Event based execution using queue etc.)
            if not queue.empty(): # process queue
                task = queue.get()
                for key in task.keys():
                    # add if key == "system"
                    if key == "write_channels":
                        if key in daq_channels:
                            daq.write_channels(task[key])
                        elif "SHED" in key:
                            update_system_variable(task[key])
                            
            t_now = datetime.now()
            sleep(0.01)
        t_next = t_next + timedelta(seconds=1)              # runs every 1 second (Slower tasks, reading daq etc)
        t_now = datetime.now()
        read_daq()
        update_calculated_variables()
        update_remote_request()
        #check alarms
        #control algorithm -> call daq.write_channels()


def update_system_variable(task):
    for key in task.key():
        if vars_sys[key]["request"] == "off" and vars_sys[key]["state"] != "alarm": 
            vars_sys[key]["request"] = "on"
            vars_sys[key]["state"] = "on"
            daq.write_channels(vars_sys[key]["state_settings"]["on"])
            #print(vars_sys)
        else:
            vars_sys[key]["request"] = "off"
            daq.write_channels(vars_sys[key]["state_settings"]["off"])
            if vars_sys["SHED1"]["request"] == vars_sys["SHED2"]["request"] == vars_sys["SHED3"]["request"]:
                daq.write_channels(vars_sys["all_off"])
            #print(vars_sys)

# def system_operation():
#     write_to_daq_dict = {}
#     for key in vars_sys.keys():
#         if vars_sys[key][request] == "off":
#             write_to_daq_dict = vars_sys[key]["state_settings"]["off"]
#         else:
#             pass
    

#--------------------- Initialize background thread --------------------------------------------------------------------

queue = Queue()
background = Thread(target=background_tasks, args=(queue,))
background.daemon = True
background.start()

#-------------------- Start flask app on wsgi server -------------------------------------------------------------------

if __name__ == '__main__':
    #socketio.run(app, host='0.0.0.0')  # used for eventlet with socketio
    serve(app, port=5000)               # used for waitress, without sockets