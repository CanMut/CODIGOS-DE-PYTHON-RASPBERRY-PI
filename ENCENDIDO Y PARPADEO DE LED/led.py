import RPi.GPIO as GPIO
import time

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(5)

GPIO.cleanup()
