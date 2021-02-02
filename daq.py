from maq20 import MAQ20
from maq20.modules.diol import DIOL
from maq20 import utilities as utils
import time

''' This class is a layer to simplify using the Maq20 api. It allows for variable names to be used instead of channel names throughout the flask application, with '''

#-----Initialize daq and assign modules to physical variables----- Could be automated to scan daq and return the module types, then name accordingly.
class dataforth():

    def __init__(self, settings):
        self.settings = settings
        self.channel_map_inputs = self.settings['channel_map_inputs']
        self.channel_map_outputs = self.settings['channel_map_outputs']
        self.channel_configs = self.settings['channel_configs']
        self.daq = MAQ20(ip_address=self.settings['host'], port=self.settings['port'])
        self.module_names = ['mod1_AI_MVDN', 'mod2_AI_TTC', 'mod3_AO_VO', 'mod4_DI_DIV20', 'mod5_DIO_DIOL', 'mod6_DIO_DIOL', 'mod7_DIO_DIOL', 'mod8_DIO_DIOL']
        self.mod1_AI_MVDN = self.daq[1]
        self.mod2_AI_TTC = self.daq[2]
        self.mod3_AO_VO = self.daq[3]
        self.mod4_DI_DIV20 = self.daq[4]
        self.mod5_DIO_DIOL = self.daq[5]
        self.mod6_DIO_DIOL = self.daq[6]
        self.mod7_DIO_DIOL = self.daq[7]
        self.mod8_DIO_DIOL = self.daq[8]
        self.module_instances = [self.mod1_AI_MVDN, self.mod2_AI_TTC, self.mod3_AO_VO, self.mod4_DI_DIV20, self.mod5_DIO_DIOL, self.mod6_DIO_DIOL, self.mod7_DIO_DIOL, self.mod8_DIO_DIOL]
        self.modules = dict(zip(self.module_names, self.module_instances))

        #-----Initialize Special Functions on DIOL modules----
        self.modules_special = []
        for channel in self.channel_configs: 
            if channel in self.channel_map_inputs: #check if input
                x = len(self.channel_map_inputs[channel]) - self.channel_map_inputs[channel].find('[')
                if self.channel_configs[channel] == "counter": #case for counter with debounce
                    module = str(self.channel_map_inputs[channel])[:-x]
                    if str(self.channel_map_inputs[channel])[-2] == '0': #case for timer 0 on input 0
                        timer = 0
                    elif str(self.channel_map_inputs[channel])[-2] == '2': #case for time 1 on input 2
                        timer = 1
                    else:
                        print("Channel name error, channel cannot be used in special function")
                    if module in self.modules_special:    #check if module already instantiated as DIOL
                        eval('self.' + module).write_special_function_2_pulse_frequency_counter_with_debounce(timer=timer, internal_trigger=1)
                    else:
                        self.modules_special.append(module)
                        exec('self.' + module + "=" + "DIOL(maq20_module=self." + module + ")")
                        eval('self.' + module).write_special_function_2_pulse_frequency_counter_with_debounce(timer=timer, internal_trigger=1)
                else:
                    pass
            else:
                x = len(self.channel_map_outputs[channel]) - self.channel_map_outputs[channel].find('[')
                if self.channel_configs[channel] == "frequency_generator": #case for frequency generator
                    module = str(self.channel_map_outputs[channel])[:-x]
                    if str(self.channel_map_outputs[channel])[-2] == '0': #case for timer 0 on input 0
                        timer = 0
                    elif str(self.channel_map_outputs[channel])[-2] == '2': #case for time 1 on input 2
                        timer = 1
                    else:
                        print("Channel name error, channel cannot be used in special function")
                    if module in self.modules_special:
                        eval('self.' + module).write_special_function_5_frequency_generator(timer=timer, frequency=0)
                    else:
                        self.modules_special.append(module)
                        exec('self.' + module + "=" + "DIOL(maq20_module=self." + module + ")")
                        eval('self.' + module).write_special_function_5_frequency_generator(timer=timer, frequency=0)
                else:
                    pass

        #----- Functions for accessing maq20 api -----

    def read_modules(self, modules): #accepts dict of module name: module instance and returns dict of module name: list of channel values
        data = {}
        for key in modules:
            if 'VDN' in key or 'TTC' in key or 'DIO' in key or 'AO' in key:
                data[key] = modules[key].read_data(0, number_of_channels=modules[key].get_number_of_channels())
            elif 'DI' in key:
                data[key] = modules[key].read_data_counts(0, number_of_channels=modules[key].get_number_of_channels())
        return data

    def read(self, channel, channel_type): #accepts channel name, returns dict of {channel name: value} and checks for enabled counters.
        channel_map = eval("self.channel_map_" + channel_type)
        x = len(channel_map[channel]) - channel_map[channel].find('[')
        if hasattr(eval("self." + str(channel_map[channel])[:-x]), 'read_special_function_2_pulse_frequency_counter_with_debounce'):    #check if module configured for DIOL
            if str(channel_map[channel])[-2] == '0':     #check if channel is counter input
                return eval("self." + str(channel_map[channel])[:-x]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=0)['Frequency']
            elif str(channel_map[channel])[-2] == '2':
                return eval("self." + str(channel_map[channel])[:-x]).read_special_function_2_pulse_frequency_counter_with_debounce(timer=1)['Frequency']
            else:
                return eval("self." + str(channel_map[channel]))           
        else:
            if 'DIV20' in str(channel_map[channel]):
                return eval("self." + str(channel_map[channel])[:-x]).read_data_counts(int(channel_map[channel][-2]), number_of_channels=1)[0]
            else:
                return eval("self." + str(channel_map[channel]))

    def read_modbus_register(self, channel): #used to read the state of DIO outputs.
        module = str(self.channel_map_outputs[channel])[:-3]
        channel_number = int(str(self.channel_map_outputs[channel])[-2])+1000
        register_value = eval('self.' + module).read_register(channel_number)
        return register_value

    def read_channels(self, channels): #accepts a list of requested channel names: eg ['T_shed2_cold': 'T_shed2_hot'] and returns dict of {channel name: values}
        data = {}
        for channel in channels:
            if channel in self.channel_map_inputs.keys(): 
                if 'DIO' in str(self.channel_map_inputs[channel]):
                    data_cur = self.read(channel, "inputs")
                    if data_cur == 1: #invert logic so 0 = 1, 1 = 0
                        data[channel] = 0
                    else:
                        data[channel] = 1
                data[channel] = self.read(channel, "inputs")
            elif channel in self.channel_map_outputs.keys():
                if 'DIO' in str(self.channel_map_outputs[channel]):
                    data_cur = self.read_modbus_register(channel)
                    if data_cur == 1: #invert logic so 0 = 1, 1 = 0
                        data[channel] = 0
                    else:
                        data[channel] = 1
                else:
                    data[channel] = self.read(channel, "outputs")
            else:
                data[channel] = 'chan_name_error'
        # call scale/calibration function and correct values before returning
        return data

    def write_channels(self, channels):    # accepts a dict of the engineering channels to write to and the desired values. Gets the physical channel from the map and writes to the physical channel.    for key, value in channels, values:
        for key in channels.keys():
            if key in self.channel_configs.keys(): # check for special function
                if self.channel_configs[key] == "frequency_generator":
                    module = str(self.channel_map_outputs[key])[:-3]
                    if str(self.channel_map_outputs[key])[-2] == '0': #case for timer 0 on input 0
                        timer = 0
                    elif str(self.channel_map_outputs[key])[-2] == '2': #case for time 1 on input 2
                        timer = 1
                    frequency = str(channels[key])
                    exec("self." + module + ".write_special_function_5_frequency_generator(timer=" + str(timer) + ", frequency=" + frequency + ")")
            else: # regular output (boolean + AO) add other function with elif statements
                if key in self.channel_map_outputs.keys():
                    if 'DIO' in str(self.channel_map_outputs[key]):
                        if channels[key] == 'true' or channels[key] == 1:
                            value = 0
                        else:
                            value = 1
                    elif 'AO' in str(self.channel_map_outputs[key]):
                        value = channels[key]
                    channel_to_write = str(self.channel_map_outputs[key])
                    exec("self." + channel_to_write + '=' + str(value))
                else:
                    pass


#-----Function Testing-----
#with open("config.txt", 'w') as outfile:
#    json.dump(settings, outfile)

'''
try:
    daq = dataforth(settings)
    channels_read = []
    for channel in settings['channel_map_inputs'].keys():
        channels_read.append(channel)
    channels_write = {}
    for channel in settings['channel_map_outputs'].keys():
        channels_write[channel] = 1
    while True:
        daq.write_channels(channels_write)
        channel = daq.read_channels(channels_read)
        print(channel)
        time.sleep(1)
except KeyboardInterrupt:
    pass
'''

   