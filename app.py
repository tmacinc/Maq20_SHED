
from flask import Flask, render_template, jsonify, request
from threading import Thread, Event
from flask_socketio import SocketIO, emit
import eventlet
from Auxiliary_In_out import InputValues
demo = 1
if demo != 1:
    import daq

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)

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
    if demo == 1:
        data = InputValues("T_shed3").input_eng
    else:
        daq.read_channels(channels_requested) #if using variable layer to background control task, switch this to update variable and have background task call this function.
    return jsonify(ajax_data=data)

@app.route('/_set_control') #Accepts requested control variable from user and sends value to controller.
def set_control():
    msg = request.args.to_dict()
    channels = list(request.args.to_dict().keys())
    channel_name = channels[0]
    print("Received request to update setting: " + channel_name + " to new value: " + msg[channel_name])
    if demo == 1:
        Pass
    else:
        daq.write_channels(msg) #if using variable layer to background control task, switch this to update variable and have background task call this function.
    return jsonify(ajax_response="Received channel -> value: " + str(channel_name) + " -> " + str(msg[channel_name]))

@app.route('/_maq20_fetch_data') #Used for maq20_overview.html
def maq20_fetch_data():
    if demo == 1:
        data = {'mod1_AI_MVDN': [-2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048], 'mod2_AI_TTC': [21.3867, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375], 'mod3_AO_VO': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'mod4_DI_DIV20': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'mod5_DIO_DIOL': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 'mod6_DIO_DIOL': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'mod7_DIO_DIOL': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'mod8_DIO_DIOL': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
    else:
        daq.read_modules(daq.modules)

    print(data)
    return jsonify(ajax_data=data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')