from maq20 import MAQ20
import time

channel_map = {
    'T_shed2_cold': 'mod2_AI_TTC[0]',
    'T_shed2_hot': 'mod2_AI_TTC[1]',
    'T_shed3_cold': 'mod2_AI_TTC[2]',
    'T_shed3_hot': 'mod2_AI_TTC[3]',
    'T_main_hot': 'mod2_AI_TTC[4]',
    'T_main_cold': 'mod2_AI_TTC[5]',
    'T_shed1_cold': 'mod2_AI_TTC[6]',
    'T_shed1_hot': 'mod2_AI_TTC[7]'
    }
#-----Initialize daq and assign modules to physical variables-----

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

def read_channels(channels): #accepts dict of the channel map, channel name: channel location. eg {'T_shed2_cold': 'mod2_AI_TTC[0]'} and returns dict of channel name: data
    data = {}
    for key in channels:
        data[key] = eval(channels[key])
    return data


data = read_channels(channel_map)
print(data)

def write_outputs(modules):
    pass

def map_channels(data, channels):
    pass
