from maq20 import MAQ20
from maq20.modules.diol import DIOL
import time


#-----Build maps for channels. Engineering variable to physical channel----- Could be called from config file.

channel_map = {
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
'Valve_shed3_hot': 'mod3_AO_VO[0]',
'Valve_shed3_cold': 'mod3_AO_VO[1]',
'Valve_shed2_hot': 'mod3_AO_VO[2]',
'Valve_shed2_cold': 'mod3_AO_VO[3]',
'Valve_main_hot': 'mod3_AO_VO[4]',
'Valve_main_cold': 'mod3_AO_VO[5]',
'Valve_shed1_cold': 'mod3_AO_VO[6]',
'Valve_shed1_hot': 'mod3_AO_VO[7]',
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
'Pump_shed3_hot': 'mod5_DIO_DIOL[0]',
'Pump_shed3_cold': 'mod5_DIO_DIOL[1]',
'Pump_shed2_hot': 'mod5_DIO_DIOL[2]',
'Pump_shed2_cold': 'mod5_DIO_DIOL[3]',
'Pump_main_hot': 'mod5_DIO_DIOL[4]',
'Flowmeter_shed3_hot': 'mod5_DIO_DIOL[5]',
'Request_shed3': 'mod5_DIO_DIOL[6]',
'Flowmeter_shed3_cold': 'mod5_DIO_DIOL[7]',
'mod5_DIO_DIOL_Placeholder9': 'mod5_DIO_DIOL[8]',
'mod5_DIO_DIOL_Placeholder10': 'mod5_DIO_DIOL[9]',
'Pump_main_cold': 'mod6_DIO_DIOL[0]',
'Pump_shed1_cold': 'mod6_DIO_DIOL[1]',
'Pump_shed1_hot': 'mod6_DIO_DIOL[2]',
'Door_shed2_seal': 'mod6_DIO_DIOL[3]',
'Exhaust_shed2': 'mod6_DIO_DIOL[4]',
'Flowmeter_shed2_hot': 'mod6_DIO_DIOL[5]',
'Request_shed2': 'mod6_DIO_DIOL[6]',
'Flowmeter_shed2_cold': 'mod6_DIO_DIOL[7]',
'mod6_DIO_DIOL_Placeholder9': 'mod6_DIO_DIOL[8]',
'mod6_DIO_DIOL_Placeholder10': 'mod6_DIO_DIOL[9]',
'Request_good_shed1': 'mod7_DIO_DIOL[0]',
'Request_good_shed2': 'mod7_DIO_DIOL[1]',
'Request_good_shed3': 'mod7_DIO_DIOL[2]',
'Door_shed3_seal': 'mod7_DIO_DIOL[3]',
'Exhaust_shed3': 'mod7_DIO_DIOL[4]',
'Flowmeter_main_hot': 'mod7_DIO_DIOL[5]',
'Exhaust_airflow_confirmed': 'mod7_DIO_DIOL[6]',
'Flowmeter_main_cold': 'mod7_DIO_DIOL[7]',
'mod7_DIO_DIOL_Placeholder9': 'mod7_DIO_DIOL[8]',
'mod7_DIO_DIOL_Placeholder10': 'mod7_DIO_DIOL[9]',
'Exhaust_damper': 'mod8_DIO_DIOL[0]',
'Exhaust_fan': 'mod8_DIO_DIOL[1]',
'mod8_DIO_DIOL_Placeholder3': 'mod8_DIO_DIOL[2]',
'mod8_DIO_DIOL_Placeholder4': 'mod8_DIO_DIOL[3]',
'mod8_DIO_DIOL_Placeholder5': 'mod8_DIO_DIOL[4]',
'Flowmeter_shed1_cold': 'mod8_DIO_DIOL[5]',
'Request_shed1': 'mod8_DIO_DIOL[6]',
'Flowmeter_shed1_hot': 'mod8_DIO_DIOL[7]',
'mod8_DIO_DIOL_Placeholder9': 'mod8_DIO_DIOL[8]',
'mod8_DIO_DIOL_Placeholder10': 'mod8_DIO_DIOL[9]'
}
#-----Initialize daq and assign modules to physical variables----- Could be a function that's called only if needed.

daq = MAQ20(ip_address="192.168.1.10", port=502)
module_names = ['mod1_AI_MVDN', 'mod2_AI_TTC', 'mod3_AO_VO', 'mod4_DI_DIV20', 'mod5_DIO_DIOL', 'mod6_DIO_DIOL', 'mod7_DIO_DIOL', 'mod8_DIO_DIOL']

mod1_AI_MVDN = daq[1]
mod2_AI_TTC = daq[2]
mod3_AO_VO = daq[3]
mod4_DI_DIV20 = daq[4]
mod5_DIO_DIOL = daq[5]
mod6_DIO_DIOL = daq[6]
mod7_DIO_DIOL = daq[7]
mod8_DIO_DIOL = daq[8]

module_instances = [mod1_AI_MVDN, mod2_AI_TTC, mod3_AO_VO, mod4_DI_DIV20, mod5_DIO_DIOL, mod6_DIO_DIOL, mod7_DIO_DIOL, mod8_DIO_DIOL]
modules = dict(zip(module_names, module_instances))

#-----Initialize Counters on DIOL moduels----

mod5_DIO_DIOL = DIOL(maq20_module=mod5_DIO_DIOL)
mod6_DIO_DIOL = DIOL(maq20_module=mod6_DIO_DIOL)
mod7_DIO_DIOL = DIOL(maq20_module=mod7_DIO_DIOL)
mod8_DIO_DIOL = DIOL(maq20_module=mod8_DIO_DIOL)

mod8_DIO_DIOL.write_special_function_5_frequency_generator(timer=0, frequency=10) # frequency generator 500 Hz

mod5_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
mod5_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
mod6_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
mod6_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
mod7_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
mod7_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)
#mod8_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)
#mod8_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=1, internal_trigger=1)

#-----Map physical channels to variables-----

def read_modules(modules): #accepts dict of module name: module instance and returns dict of module name: list of channel values
    data = {}
    for key in modules:
        print(key)
        if 'VDN' in key or 'TTC' in key or 'DIO' in key or 'AO' in key:
            data[key] = modules[key].read_data(0, number_of_channels=modules[key].get_number_of_channels())
        elif 'DI' in key:
            data[key] = modules[key].read_data_counts(0, number_of_channels=modules[key].get_number_of_channels())
    return data

def read(channel): #accepts channel name, returns dict of {channel name: value} and checks for enabled counters.
    if hasattr(eval(channel_map[channel][:-3]), 'read_special_function_2_pulse_frequency_counter_with_debounce'):    #check if module configured for DIOL
        if channel_map[channel][-2] == '0':     #check if channel is counter input
            return eval(channel_map[channel][:-3]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=0)['Frequency']
        elif channel_map[channel][-2] == '2':
            return eval(channel_map[channel][:-3]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=1)['Frequency']
        else:
            return eval(channel_map[channel])           
    else:
        if 'DIV20' in channel_map[channel]:
            return eval(channel_map[channel][:-3]).read_data_counts(int(channel[-2]), number_of_channels=1)[0]
        return eval(channel_map[channel])

def read_channels(channels): #accepts a list of requested channel names: eg ['T_shed2_cold': 'T_shed2_hot'] and returns dict of {channel name: values}
    data = {}
    for channel in channels:
        if channel in channel_map.keys():
            data[channel] = read(channel)
        else:
            data[channel] = 'chan_name_error'
    return data
     
def write_channels(channels):    # accepts a dict of the engineering channels to write to and the desired values. Gets the physical channel from the map and writes to the physical channel.    for key, value in channels, values:
    err = False
    for key in channels:
        if key in channel_map.keys():
            print(key, channel_map[key], channels[key])
            channel_map[key] = channels[key]
        else:
            err = True
    return err

#-----Function Testing-----

#channels = ['T_shed3_l', 'Door_shed2_seal', 'Pump_main_cold']
#channels = ['Pump_main_hot', 'T_main_hot', 'Valve_main_hot', 'DIV20_Placeholder_11', 'Pump_main_cold', 'T_main_cold', 'Valve_main_cold']

#try:
#    while True:
#        print(read_channels(channels))
#        time.sleep(1)
#except KeyboardInterrupt:
#    pass
