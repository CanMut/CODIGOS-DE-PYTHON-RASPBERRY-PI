import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led_1 = 10 #verde
led_2 = 12 #naranja
led_3 = 16 #rojo
led_pv = 11#led verde peaton
led_pr =13#led rojo peaton
led_list = [12,13]
Boton = 5


GPIO.setup(led_3, GPIO.OUT)#led rojo
GPIO.setup(led_2, GPIO.OUT)#led naranja
GPIO.setup(led_1, GPIO.OUT)#led verde
GPIO.setup(led_pv, GPIO.OUT)#led peaton verde
GPIO.setup(led_pr, GPIO.OUT)#led peaton rojo
GPIO.setup(Boton, GPIO.IN, GPIO.PUD_UP)


def peaton():#al presionar el boton
    for i in range(0,25):#parpadeo de led amarillo y rojo del peaton
            GPIO.output(led_list, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led_list, GPIO.LOW)
            time.sleep(0.2)
    time.sleep(0.2)
    GPIO.output(led_1, GPIO.LOW)#apagar led verde peaton
    GPIO.output(led_2, GPIO.LOW)#apagar led amarillo peaton
    GPIO.output(led_3, GPIO.HIGH)#prender led rojo peaton
    GPIO.output(led_pr, GPIO.LOW)#apagar led rojo peaton
    GPIO.output(led_pv, GPIO.HIGH)#prender led verde peaton
    time.sleep(15)
    for i in range(0,25):#parpadeo del led verde peaton
        GPIO.output(led_pv, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_pv, GPIO.HIGH)
        time.sleep(0.2)

GPIO.output(led_pr, GPIO.HIGH)#prender led rojo peaton
GPIO.output(led_pv, GPIO.LOW)#apagar led verde peaton
GPIO.output(led_2, GPIO.LOW)#apagar led amarillo
GPIO.output(led_3, GPIO.LOW)#apagar led rojo
GPIO.output(led_1, GPIO.HIGH)#prender el led verde
time.sleep(10)#10 segundos le toca estar encendido
GPIO.output(led_1, GPIO.LOW)#apagar el led verde
GPIO.output(led_2, GPIO.HIGH)#prender el led amarillo
time.sleep(5)#5 segundos le toca estar encendido
for i in range(0,25):#parpadeo del led amarillo
    GPIO.output(led_2, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(led_2, GPIO.HIGH)
    time.sleep(0.2)
time.sleep(0.05)
GPIO.output(led_2, GPIO.LOW) #apagar el led amarillo
GPIO.output(led_3, GPIO.HIGH) #prender el led rojo
time.sleep(10) #10 segundos le toca estar encendido
while True:
    if (GPIO.input(Boton)):
        peaton()
    
print ( "Limpiando la configuración de los GPIO" )
GPIO.cleanup()