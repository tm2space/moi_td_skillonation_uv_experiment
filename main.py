# main.py

import time
from moi_obc_interface import *

# Define the resolution for printed values
PRINT_RESOLUTION = 4  # Number of decimal places

def main():
    moi_interface = MoiOBCInterface()
    sensor_channel = 6
    uv_sensor = moi_interface.initialize_sensor(sensor_channel)

    # Configure the uv_sensor
    uv_sensor.gain = sensor_lib.GAIN_512X
    uv_sensor.integration_time = sensor_lib.INTEGRATION_TIME_128MS
    
    #delay time for sensor to initialise
    time.sleep(1.5)

    # Main loop to read values
    while True:
        uva, uvb, uvc, temp = uv_sensor.values
        print(f'uva: {uva:.{PRINT_RESOLUTION}f}, uvb: {uvb:.{PRINT_RESOLUTION}f}, uvc: {uvc:.{PRINT_RESOLUTION}f}, temp: {temp: 1.2f}')
        time.sleep(2)

if __name__ == "__main__":
    main()
