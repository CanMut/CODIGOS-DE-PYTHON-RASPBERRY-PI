import RPi.GPIO as GPIO

Ena = 14
In1 = 15
In2 = 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(Ena,100)
pwm.start(0)
 
while True:
    GPIO.output(In1,GPIO.HIGH)
    GPIO.output(In2,GPIO.LOW)
    pwm.ChangeDutyCycle(100)
    

    
