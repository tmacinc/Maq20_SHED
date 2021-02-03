import time
import random
import json

with open('config.json') as json_file:
    settings = json.load(json_file)
calibration = settings["calibration"]
print (calibration)

# for use with pulse counter instead of frequency
flow_count = {
        'Flowmeter_shed3_hot':  [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_shed3_cold': [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_shed2_hot':  [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_shed2_cold': [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_main_hot':   [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_main_cold':  [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_shed1_hot':  [0,time.time()],  # [previous pulse count, previous time]
        'Flowmeter_shed1_cold': [0,time.time()],  # [previous pulse count, previous time]
    }

def pulse_to_frequency(key, value):
    prev_count = flowcount[key][0]
    current_count = value
    prev_time = flowcount[key][1]
    current_time = time.time()
    sample_time = (current_time - prev_time)  ## sample time in seconds
    frequency = (current_count - prev_count) / (sample_time)
    return frequency

def frequency_to_flowrate(frequency,key):
    flowrate = round(frequency * 60 / calibration[key], 2)                    ## Hz / ppg = gal/min
    return flowrate

demo_daq = {
    'mod1_AI_MVDN': [-2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048, -2.988048],
    'mod2_AI_TTC': [21.3867, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375, -585.9375], 
    'mod3_AO_VO': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    'mod4_DI_DIV20': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    'mod5_DIO_DIOL': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    'mod6_DIO_DIOL': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    'mod7_DIO_DIOL': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    'mod8_DIO_DIOL': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }
        
def read_channels_demo():

    for key,value in demo_daq.items():
        if "mod1" in key:
            for i in range(0,len(value)):
                demo_daq[key][i] = random.uniform(0.4,  .5)
        elif "mod2" in key:
            for i in range(0,len(value)):
                demo_daq[key][i] = random.uniform(10,65)
        else: 
            pass
    
    return demo_daq

def demo_data():
    demo_data = {
        
    }

def raw_to_eng(data):
    """
    data is the dictionary passed from the daw during the input. 
    
    return: new_data dictionary with values changed from raw values to engineering values
    """
    new_data = {}
    for key in data.keys():
        if key.endswith("_l", 7,9) or key.endswith("_r", 7,9):
            new_data[key] = round(float(data[key]*calibration[key]),2)
        elif key.startswith("Flowmeter_"):
            new_data[key] = round(frequency_to_flowrate(data[key],key),2)
        else:
            new_data[key] = round(data[key], 2)
    if "T_shed2" in data.keys():
        new_data["T_shed2"] = round((new_data["T_shed2_l"] + new_data["T_shed2_r"]) / 2, 2)
    if "T_shed3" in data.keys():
        new_data["T_shed3"] = round((new_data["T_shed3_l"] + new_data["T_shed3_r"]) / 2, 2)

    return new_data

print(read_channels_demo())



