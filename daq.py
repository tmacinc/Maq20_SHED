from maq20 import MAQ20
import time


#-----Build maps for channels. Engineering variable to physical channel----- Could be called from config file.

channel_map_inputs = {
    'T_shed2_cold': 'mod2_AI_TTC[0]',
    'T_shed2_hot': 'mod2_AI_TTC[1]',
    'T_shed3_cold': 'mod2_AI_TTC[2]',
    'T_shed3_hot': 'mod2_AI_TTC[3]',
    'T_main_hot': 'mod2_AI_TTC[4]',
    'T_main_cold': 'mod2_AI_TTC[5]',
    'T_shed1_cold': 'mod2_AI_TTC[6]',
    'T_shed1_hot': 'mod2_AI_TTC[7]'
    }

channel_map_outputs = {
    'Valve_shed2_hot': 'mod3_AO_VO[0]',
    'Valve_shed2_cold': 'mod3_AO_VO[1]'
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

def read_channels(channels): #accepts a list of requested channel names: eg ['T_shed2_cold': 'T_shed2_hot'] and returns dict of {channel name: values}
    data = {}
    for channel in channels:
        if channel in channel_map_inputs.keys():
            print(channel)
            data[channel] = eval(channel_map_inputs[channel])
        elif channel in channel_map_outputs.keys():
            print(channel)
            data[channel] = channel_map_outputs[channel]
        else:
            data[channel] = 'chan_name_error'
    return data

def write_channels(channels):    # accepts a dict of the engineering channels to write to and the desired values. Gets the physical channel from the map and writes to the physical channel.    for key, value in channels, values:
    err = False
    for key in channels:
        if key in channel_map_outputs.keys():
            print(key, channel_map_outputs[key], channels[key])
            channel_map_outputs[key] = channels[key]
        else:
            err = True
    return err