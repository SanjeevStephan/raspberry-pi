
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

try:
	while True:
	     GPIO.output(8,True)
    	     time.sleep(4)
             # GPIO.output(8,False)
              #time.sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()
