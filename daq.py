from maq20 import MAQ20
from maq20.modules.diol import DIOL
from maq20 import utilities as utils
import time


#-----Build maps for channels. Engineering variable to physical channel----- Could be called from config file.

channel_map_inputs = {
'T_shed2_l': 'mod1_AI_MVDN[0]',
'T_shed2_r': 'mod1_AI_MVDN[1]',
'T_shed3_l': 'mod1_AI_MVDN[2]',
'T_shed3_r': 'mod1_AI_MVDN[3]',
'Gas_analyzer_shed2': 'mod1_AI_MVDN[4]',
'Gas_analyzer_shed3': 'mod1_AI_MVDN[5]',
'MVDN_Placeholder_7': 'mod1_AI_MVDN[6]',
'MVDN_Placeholder_8': 'mod1_AI_MVDN[7]',
'T_shed2_cold': 'mod2_AI_TTC[0]',
'T_shed2_hot': 'mod2_AI_TTC[1]',
'T_shed3_cold': 'mod2_AI_TTC[2]',
'T_shed3_hot': 'mod2_AI_TTC[3]',
'T_main_hot': 'mod2_AI_TTC[4]',
'T_main_cold': 'mod2_AI_TTC[5]',
'T_shed1_cold': 'mod2_AI_TTC[6]',
'T_shed1_hot': 'mod2_AI_TTC[7]',
'DIV20_Placeholder_1': 'mod4_DI_DIV20[0]',
'DIV20_Placeholder_2': 'mod4_DI_DIV20[1]',
'DIV20_Placeholder_3': 'mod4_DI_DIV20[2]',
'DIV20_Placeholder_4': 'mod4_DI_DIV20[3]',
'DIV20_Placeholder_5': 'mod4_DI_DIV20[4]',
'DIV20_Placeholder_6': 'mod4_DI_DIV20[5]',
'DIV20_Placeholder_7': 'mod4_DI_DIV20[6]',
'DIV20_Placeholder_8': 'mod4_DI_DIV20[7]',
'DIV20_Placeholder_9': 'mod4_DI_DIV20[8]',
'DIV20_Placeholder_10': 'mod4_DI_DIV20[9]',
'DIV20_Placeholder_11': 'mod4_DI_DIV20[1]',
'DIV20_Placeholder_12': 'mod4_DI_DIV20[11]',
'DIV20_Placeholder_13': 'mod4_DI_DIV20[12]',
'DIV20_Placeholder_14': 'mod4_DI_DIV20[13]',
'DIV20_Placeholder_15': 'mod4_DI_DIV20[14]',
'DIV20_Placeholder_16': 'mod4_DI_DIV20[15]',
'DIV20_Placeholder_17': 'mod4_DI_DIV20[16]',
'DIV20_Placeholder_18': 'mod4_DI_DIV20[17]',
'DIV20_Placeholder_19': 'mod4_DI_DIV20[18]',
'DIV20_Placeholder_20': 'mod4_DI_DIV20[19]',
'Flowmeter_shed3_hot': 'mod5_DIO_DIOL[0]',
'Request_shed3': 'mod5_DIO_DIOL[1]',
'Flowmeter_shed3_cold': 'mod5_DIO_DIOL[2]',
'mod5_DIO_DIOL_Placeholder9': 'mod5_DIO_DIOL[3]]',
'mod5_DIO_DIOL_Placeholder10': 'mod5_DIO_DIOL[4]',
'Flowmeter_shed2_hot': 'mod6_DIO_DIOL[0]',
'Request_shed2': 'mod6_DIO_DIOL[1]',
'Flowmeter_shed2_cold': 'mod6_DIO_DIOL[2]',
'mod6_DIO_DIOL_Placeholder9': 'mod6_DIO_DIOL[3]',
'mod6_DIO_DIOL_Placeholder10': 'mod6_DIO_DIOL[4]',
'Flowmeter_main_hot': 'mod7_DIO_DIOL[0]',
'Exhaust_airflow_confirmed': 'mod7_DIO_DIOL[1]',
'Flowmeter_main_cold': 'mod7_DIO_DIOL[2]',
'mod7_DIO_DIOL_Placeholder9': 'mod7_DIO_DIOL[3]',
'mod7_DIO_DIOL_Placeholder10': 'mod7_DIO_DIOL[4]',
'Flowmeter_shed1_cold': 'mod8_DIO_DIOL[0]',
'Request_shed1': 'mod8_DIO_DIOL[1]',
'Flowmeter_shed1_hot': 'mod8_DIO_DIOL[2]',
'mod8_DIO_DIOL_Placeholder9': 'mod8_DIO_DIOL[3]',
'mod8_DIO_DIOL_Placeholder10': 'mod8_DIO_DIOL[4]'
}
channel_map_outputs = {
    'Valve_shed3_hot': 'mod3_AO_VO[0]',
    'Valve_shed3_cold': 'mod3_AO_VO[1]',
    'Valve_shed2_hot': 'mod3_AO_VO[2]',
    'Valve_shed2_cold': 'mod3_AO_VO[3]',
    'Valve_main_hot': 'mod3_AO_VO[4]',
    'Valve_main_cold': 'mod3_AO_VO[5]',
    'Valve_shed1_cold': 'mod3_AO_VO[6]',
    'Valve_shed1_hot': 'mod3_AO_VO[7]',
    'Pump_shed3_hot': 'mod5_DIO_DIOL[0]',
    'Pump_shed3_cold': 'mod5_DIO_DIOL[1]',
    'Pump_shed2_hot': 'mod5_DIO_DIOL[2]',
    'Pump_shed2_cold': 'mod5_DIO_DIOL[3]',
    'Pump_main_hot': 'mod5_DIO_DIOL[4]',
    'Pump_main_cold': 'mod6_DIO_DIOL[0]',
    'Pump_shed1_cold': 'mod6_DIO_DIOL[1]',
    'Pump_shed1_hot': 'mod6_DIO_DIOL[2]',
    'Door_shed2_seal': 'mod6_DIO_DIOL[3]',
    'Exhaust_shed2': 'mod6_DIO_DIOL[4]',
    'Request_good_shed1': 'mod7_DIO_DIOL[0]',
    'Request_good_shed2': 'mod7_DIO_DIOL[1]',
    'Request_good_shed3': 'mod7_DIO_DIOL[2]',
    'Door_shed3_seal': 'mod7_DIO_DIOL[3]',
    'Exhaust_shed3': 'mod7_DIO_DIOL[4]',
    'Exhaust_damper': 'mod8_DIO_DIOL[0]',
    'Exhaust_fan': 'mod8_DIO_DIOL[1]',
    'mod8_DIO_DIOL_Placeholder3': 'mod8_DIO_DIOL[2]',
    'mod8_DIO_DIOL_Placeholder4': 'mod8_DIO_DIOL[3]',
    'mod8_DIO_DIOL_Placeholder5': 'mod8_DIO_DIOL[4]',    
}

#-----Define special channel types-----

channel_configs = {
    "Exhaust_damper": "frequency_generator",
    'Flowmeter_shed1_hot': 'counter',
    'Flowmeter_shed1_cold': 'counter',
    'Flowmeter_shed2_hot': 'counter',
    'Flowmeter_shed2_cold': 'counter',
    'Flowmeter_shed3_hot': 'counter',
    'Flowmeter_shed3_cold': 'counter',
    'Flowmeter_main_hot': 'counter',
    'Flowmeter_main_cold': 'counter',
}

#-----Initialize daq and assign modules to physical variables----- Could be automated to scan daq and return the module types, then name accordingly.

#def initialize_daq():
#    global daq 
daq = MAQ20(ip_address="192.168.1.10", port=502)
module_names = ['mod1_AI_MVDN', 'mod2_AI_TTC', 'mod3_AO_VO', 'mod4_DI_DIV20', 'mod5_DIO_DIOL', 'mod6_DIO_DIOL', 'mod7_DIO_DIOL', 'mod8_DIO_DIOL']
"""
global mod1_AI_MVDN
global mod2_AI_TTC
global mod3_AO_VO
global mod4_DI_DIV20 
global mod5_DIO_DIOL 
global mod6_DIO_DIOL
global mod7_DIO_DIOL
global mod8_DIO_DIOL
"""
mod1_AI_MVDN = daq[1]
mod2_AI_TTC = daq[2]
mod3_AO_VO = daq[3]
mod4_DI_DIV20 = daq[4]
mod5_DIO_DIOL = daq[5]
mod6_DIO_DIOL = daq[6]
mod7_DIO_DIOL = daq[7]
mod8_DIO_DIOL = daq[8]

module_instances = [mod1_AI_MVDN, mod2_AI_TTC, mod3_AO_VO, mod4_DI_DIV20, mod5_DIO_DIOL, mod6_DIO_DIOL, mod7_DIO_DIOL, mod8_DIO_DIOL]
#    global modules 
modules = dict(zip(module_names, module_instances))
#-----Initialize Special Functions on DIOL modules----
modules_special = []
for channel in channel_configs: 
    if channel in channel_map_inputs: #check if input
        if channel_configs[channel] == "counter": #case for counter with debounce
            module = str(channel_map_inputs[channel])[:-3]
            if str(channel_map_inputs[channel])[-2] == '0': #case for timer 0 on input 0
                timer = 0
            elif str(channel_map_inputs[channel])[-2] == '2': #case for time 1 on input 2
                timer = 1
            else:
                print("Channel name error, channel cannot be used in special function")
            if module in modules_special:    #check if module already instantiated as DIOL
                eval(module).write_special_function_2_pulse_frequency_counter_with_debounce(timer=timer, internal_trigger=1)
            else:
                modules_special.append(module)
                exec(module + "=" + "DIOL(maq20_module=" + module + ")")
                #eval(module) = DIOL(maq20_module=eval(module))
                eval(module).write_special_function_2_pulse_frequency_counter_with_debounce(timer=timer, internal_trigger=1)
#            print(dir(eval(module)))
        else:
            pass
    else:
        if channel_configs[channel] == "frequency_generator": #case for frequency generator
            module = str(channel_map_outputs[channel])[:-3]
            if str(channel_map_outputs[channel])[-2] == '0': #case for timer 0 on input 0
                timer = 0
            elif str(channel_map_outputs[channel])[-2] == '2': #case for time 1 on input 2
                timer = 1
            else:
                print("Channel name error, channel cannot be used in special function")
            if module in modules_special:
                eval(module).write_special_function_5_frequency_generator(timer=timer, frequency=0)
            else:
                modules_special.append(module)
                exec(module + "=" + "DIOL(maq20_module=" + module + ")")
                eval(module).write_special_function_5_frequency_generator(timer=timer, frequency=0)
        else:
            pass
'''
#mod5_DIO_DIOL = DIOL(maq20_module=mod5_DIO_DIOL)
mod6_DIO_DIOL = DIOL(maq20_module=mod6_DIO_DIOL)
mod7_DIO_DIOL = DIOL(maq20_module=mod7_DIO_DIOL)
#mod8_DIO_DIOL = DIOL(maq20_module=mod8_DIO_DIOL)

#mod8_DIO_DIOL.write_special_function_5_frequency_generator(timer=0, frequency=10) # frequency generator 500 Hz
#mod5_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
#mod5_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
mod6_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
mod6_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
mod7_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
mod7_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
#mod8_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
#mod8_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
'''
#----- Functions for accessing maq20 api -----

def read_modules(modules): #accepts dict of module name: module instance and returns dict of module name: list of channel values
    data = {}
    for key in modules:
        if 'VDN' in key or 'TTC' in key or 'DIO' in key or 'AO' in key:
            data[key] = modules[key].read_data(0, number_of_channels=modules[key].get_number_of_channels())
        elif 'DI' in key:
            data[key] = modules[key].read_data_counts(0, number_of_channels=modules[key].get_number_of_channels())
    return data

def read(channel, channel_type): #accepts channel name, returns dict of {channel name: value} and checks for enabled counters.
    channel_map = eval("channel_map_" + channel_type)
    if hasattr(eval(str(channel_map[channel])[:-3]), 'read_special_function_2_pulse_frequency_counter_with_debounce'):    #check if module configured for DIOL
        if str(channel_map[channel])[-2] == '0':     #check if channel is counter input
            return eval(str(channel_map[channel])[:-3]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=0)['Frequency']
        elif str(channel_map[channel])[-2] == '2':
            return eval(str(channel_map[channel])[:-3]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=1)['Frequency']
        else:
            return eval(str(channel_map[channel]))           
    else:
        if 'DIV20' in str(channel_map[channel]):
            return eval(str(channel_map[channel])[:-3]).read_data_counts(int(channel[-2]), number_of_channels=1)[0]
        else:
            return eval(str(channel_map[channel]))

def read_modbus_register(channel): #used to read the state of DIO outputs.
    module = str(channel_map_outputs[channel])[:-3]
    channel_number = int(str(channel_map_outputs[channel])[-2])+1000
    register_value = eval(module).read_register(channel_number)
    return register_value

def read_channels(channels): #accepts a list of requested channel names: eg ['T_shed2_cold': 'T_shed2_hot'] and returns dict of {channel name: values}
    data = {}
    for channel in channels:
        if channel in channel_map_inputs.keys(): 
            data[channel] = read(channel, "inputs")
        elif channel in channel_map_outputs.keys():
            if 'DIOL' in str(channel_map_outputs[channel]):
                data_cur = read_modbus_register(channel)
                if data_cur == 1: #invert logic so 0 = 1, 1 = 0
                    data[channel] = 0
                else:
                    data[channel] = 1
                #data[channel] = read_modbus_register(channel)
            else:
                data[channel] = read(channel, "outputs")
        else:
            data[channel] = 'chan_name_error'
    # call scale/calibration function and correct values before returning
    return data

def write_channels(channels):    # accepts a dict of the engineering channels to write to and the desired values. Gets the physical channel from the map and writes to the physical channel.    for key, value in channels, values:
    for key in channels.keys():
        if key in channel_configs.keys(): # check for special function
            if channel_configs[key] == "frequency_generator":
                module = str(channel_map_outputs[key])[:-3]
                if str(channel_map_outputs[key])[-2] == '0': #case for timer 0 on input 0
                    timer = 0
                elif str(channel_map_outputs[key])[-2] == '2': #case for time 1 on input 2
                    timer = 1
                frequency = str(channels[key])
                exec(module + ".write_special_function_5_frequency_generator(timer=" + str(timer) + ", frequency=" + frequency + ")")
        else: # regular output (boolean) add other function with elif statements
            if key in channel_map_outputs.keys():
                if channels[key] == 'true' or channels[key] == 1:
                    value = 0
                else:
                    value = 1
                channel_to_write = str(channel_map_outputs[key])
                exec(channel_to_write + '=' + str(value))
            else:
                pass

#initialize_daq()

#-----Function Testing-----

#channels = ['T_shed3_l', 'Door_shed2_seal', 'Pump_main_cold']
#channels = ['Pump_main_hot', 'T_main_hot', 'Valve_main_hot', 'DIV20_Placeholder_11', 'Pump_main_cold', 'T_main_cold', 'Valve_main_cold']
#module = {'mod6_DIO_DIOL': mod6_DIO_DIOL}

#try:
#    while True:
#        channels = {'Exhaust_damper': '65'}
#        write_channels(channels)
#        print(channels)
#        time.sleep(1)
#except KeyboardInterrupt:
#    pass
