from maq20 import MAQ20
from maq20.modules.diol import DIOL
import time

daq = MAQ20(ip_address="192.168.1.10", port=502)

mod8_DIO_DIOL = daq[8]
mod5_DIO_DIOL = daq[5]

if mod8_DIO_DIOL is not None: # Check if module was found
    mod8_DIO_DIOL = DIOL(maq20_module=mod8_DIO_DIOL)
else:
    raise TypeError("Module not found.")
if mod5_DIO_DIOL is not None:
    mod5_DIO_DIOL = DIOL(maq20_module=mod5_DIO_DIOL)
else:
    raise TypeError("Module not found.")


mod8_DIO_DIOL.write_special_function_5_frequency_generator(timer=0, frequency=10) # frequency generator 500 Hz
mod5_DIO_DIOL.write_special_function_2_pulse_frequency_counter_with_debounce(timer=0, internal_trigger=1)

try:
    while True:
        print(mod5_DIO_DIOL.read_special_function_2_pulse_frequency_counter_with_debounce(timer=0)['Frequency'], mod5_DIO_DIOL[3]) # read back the special function settings using timer 
        time.sleep(1)

except KeyboardInterrupt:
    print("Caught keyboard interrupt")