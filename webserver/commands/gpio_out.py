import sys
import RPi.GPIO as GPIO
import time

if len(sys.argv) != 3:
    print('usage: python ' + sys.argv[0] + '<gpio_pin> <state> ')
    exit(1)
pin =int( sys.argv[1])
state=int(sys.argv[2])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)


GPIO.output(pin,state)
time.sleep(1)
