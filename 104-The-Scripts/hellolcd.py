#! /usr/bin/env python
import drivers
from time import sleep
display	= drivers.Lcd()
try: 
	while True:
		print("writing to lcd")
		display.lcd_display_string("Sanjeev",1)
		sleep(3)
		display.lcd_clear()
except KeyboardInterrupt:
	print("cl3aring up ")
	display.lcd_clear()
