import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)

Lampara = 5 
Ventilador =7 

GPIO.setup(Lampara, GPIO.OUT)
GPIO.setup(Ventilador, GPIO.OUT)



GPIO.output(Lampara, True)#ensender lampara
time.sleep(1)
GPIO.output(Lampara ,False)#apagar lampara
time.sleep(1)
GPIO.output(Ventilador, True)#ensender ventilador
time.sleep(1)
GPIO.output(Ventilador, False)#apagar ventilador
time.sleep(1)