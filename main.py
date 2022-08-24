
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
#r1
GPIO.setup(21,GPIO.OUT)
#r2
GPIO.setup(26,GPIO.OUT)
try:
    while True:
        now = datetime.datetime.now().time()
        if now.hour == 16 and now.minute ==47:
            GPIO.output(21, GPIO.LOW)

        elif now.hour == 16 and now.minute ==48:
            GPIO.output(26, GPIO.LOW)

        elif now.hour == 16 and now.minute == 49:
             GPIO.output(21, GPIO.HIGH)
             print('Relay 1 OFF')
             GPIO.output(26, GPIO.HIGH)
             print('Relay 2 OFF')

finally:
    GPIO.cleanup()