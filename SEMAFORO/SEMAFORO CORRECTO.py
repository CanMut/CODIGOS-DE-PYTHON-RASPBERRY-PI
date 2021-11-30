# nano semaforo.py
#luego presiona Enter y comienza a escribir tu programa :-D 

import RPi.GPIO as GPIO
import time

led_1 = 10 #verde
led_2 = 12 #naranja
led_3 = 16 #rojo

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#led rojo
GPIO.setup(led_3, GPIO.OUT)
#led naranja
GPIO.setup(led_2, GPIO.OUT)
#led verde
GPIO.setup(led_1, GPIO.OUT)

while True:
  #prender el led verde
  GPIO.output(led_1, GPIO.HIGH)
  #10 segundos le toca estar encendido
  time.sleep(10)
  #apagar el led verde y encender el led amarillo
  GPIO.output(led_1, GPIO.LOW)
  GPIO.output(led_2, GPIO.HIGH)
  #5 segundos le toca estar encendido
  time.sleep(5)
  for i in ranger(0,25):#parpadeo del led amarillo
      GPIO.output(led_2, GPIO.LOW)
      time.sleep(0.2)
      GPIO.output(led_2, GPIO.HIGH)
      time.sleep(0.2)
  #apagar el led amarillo y encender el led rojo
  GPIO.output(led_2, GPIO.LOW)
  GPIO.output(led_3, GPIO.HIGH)
  #10 segundos le toca estar encendido
  time.sleep(10)
  #apagar el led rojo
  GPIO.output(led_3, GPIO.LOW)
  
  print ( "Limpiando la configuración de los GPIO" )
GPIO . cleanup () ## Hago una limpieza de los GPIO