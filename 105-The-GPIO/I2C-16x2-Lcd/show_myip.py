#! /usr/bin/env python

import drivers
from time import sleep
from subprocess import check_output

display = drivers.Lcd() 

IP = check_output(["hostname", "-I"]).split()[0] #fetching ip from system_info
try:
    print("Writing to display")
    while True:
        # Display My IP Address
	display.lcd_display_string("SmartHome",1) # Here '1' is first row
        display.lcd_display_string(str(IP), 2) #Here '2' is second row
        # Uncomment the following line to loop with 1 sec delay
        # sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
