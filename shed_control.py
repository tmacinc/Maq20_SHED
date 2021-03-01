import random
import json


with open('config.json') as json_file:
    settings = json.load(json_file)
calibration = settings["calibration"]
vars_sys = settings["system_variables"]
shed1_state_settings = settings["system_variables"]["SHED1"]["state"]
shed1_alarm_limits = settings["system_variables"]["SHED1"]["alarm_limits"]      # includes the state_settings (off, in range, alarm, precondition, out of range)

class alarm():
    def __init__(self, name, settings):
        self.settings = settings
        self.name = name
        self.state = settings["state"]
        self.type = settings["limit_type"]
        self.limit_high = settings["limits"]["high"]
        self.limit_low = settings["limits"]["low"]
        self.active_config = settings["active_config"]

    def update_state(self, reading):
        if self.state == 0: 
            if self.type == "inside":
                if float(reading) > float(self.limit_high) or float(reading) < float(self.limit_low):
                    self.state = 1
        elif self.state == 1:
            pass
    
    def reset(self):
        self.state = 0

    def alarm_output(self):
        return self.active_config

    def change_limit(self, limit, lim_set):
        """
        lim name: name from javascript including "high_" or "low_" as the prefix
        lim_set: set limit value entered in web interface
        """
        if limit == "low" and lim_set.isnumeric():
            self.limit_low = lim_set
        if limit == "high" and lim_set.isnumeric():
            self.limit_high = lim_set


def deadhead_protection(vars_eng):
    pass
def status_monitor(vars_eng):
    pass
def alarm_monitor(vars_eng):
    state_output = {"SHED1":'', "SHED2":'', "SHED3":''}
    for key in vars_sys.keys(): #SHED1, SHED2, SHED3
        for key2 in vars_sys[key]["alarm_limits"]["high"].keys(): #variable in ["alarm_limits"]["high"]
            if vars_eng[key2]  > vars_sys[key]["alarm_limits"]["high"][key2] :
                state[key] = "alarm"            
                 #vars_sys[key]["state"] = settings["system_variables"][key]["state"]["alarm"]
        for key2 in vars_sys[key]["alarm_limits"]["low"].keys(): #variable in ["alarm_limits"]["low"]
            if vars_eng[key2]  < vars_sys[key]["alarm_limits"]["low"][key2]:
                state[key] = "alarm"
                #vars_sys[key]["state"] = settings["system_variables"][key]["state"]["alarm"]
    return state

def flow_monitor(vars_eng):
    state = {"SHED1":'', "SHED2":'', "SHED3":''}


def SHED_control(SHED):
    """
    param: SHED(n) dictionary
    return: output_dict -> to be used in daq_write() function
    ALSO change SHED_status state
    """
    output_dict = {}


    return output_dict



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
            pass
    #return alarm_output

   
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
            elif new_dict[key][0] == 2:
                pass
            else:
                new_dict[key][0] = 0
    return new_dict