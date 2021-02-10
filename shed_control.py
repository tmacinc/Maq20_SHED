import random
import json


with open('config.json') as json_file:
    settings = json.load(json_file)
calibration = settings["calibration"]


def SHED_control(SHED):# Action when User Input toggles SHED(n) state
    """
    param: SHED(n) dictionary
    return: output_dict -> to be used in daq_write() function
    ALSO change SHED_status state
    """
    output_dict = {}

    if SHED_status[SHED]['state'] == 0:
        SHED_status[SHED]['state'] = 1
        output_dict  = SHED_status[SHED]['active_config']
    elif SHED_status[SHED]['state'] == 1 or SHED_status[SHED]['state'] == 2:
        SHED_status[SHED]['state'] = 0
        output_dict = SHED_status[SHED]['inactive_config']
    else: # SHED_status == 3 ##> Alarm function RESET ALARM and turn all function off
        SHED_status[SHED]['state'] = 0
        output_dict = SHED_status[SHED]['inactive_config']  
    
    return output_dict

def SHED_ready(SHED_status_dict, var_eng_dict): #Action to confirm if SHED is ready
    for key in SHED_status_dict.keys():
        if SHED_status_dict[key]["state"] == 1 or


def shed_status_check(var_eng_dict, status_dict):
    status_output = {}



def alarm_response(alarm_dict):
    alarm_output = {}
    for key in alarm_dict.keys():
        if alarm_dict[key]["state"] ==2: #alarm acknowledged, but still active
            pass
        if alarm_dict[key]["state"] == 1: # alarm active, not acknowledged
            for key2 in alarm_dict[key]["active_config"].keys():
                alarm_output[key2] = alarm_dict[key]["active_config"][key2]  
        if alarm_dict[key]["state"] == 0:
    return alarm_output

   
def alarm_limit_check(var_eng_dict,alarm_dict):
    """
    Input Upated Engineering Variables to compare to limits set in alarms dict
    Return: Alarm dict with updated alarm status in ["alarm_desctiption"][0] to be updated in main app.py
    """
  new_dict = {}
  for key in alarm_dict.keys():
    if alarm_dict[key][0] == 2:  ## Possible use of "alarm acknowleged but still active"
        if alarm_dict[key]["limit_type"] == "inside":
            if var_eng_dict[key] > new_dict[key][1] and var_eng_dict[key] < new_dict[key][2]: # alarm acknowledged and eng_vals inside of limits
                new_dict[key][0] = 0
        
    elif alarm_dict[key][0] == 0:
        if alarm_dict[key]["limit_type"] == "inside":
            if var_eng_dict[key] < alarm_dict[key][1] or var_eng_dict[key] > alarm_dict[key][2]: # Alarm not previously triggered and eng_vals outside of alarm 
                new_dict[key][0] = 1  # change alarm to active
        elif new_dict[key][0] == 2 and 
        else:
            new_dict[key][0] = 0
    return new_dict
