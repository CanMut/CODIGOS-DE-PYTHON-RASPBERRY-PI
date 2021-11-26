#Programa que genera las medidas de humedad del suelo del sensor.

import RPi.GPIO as GPIO #Libreria para utilizar las GPIO.
import time 		#Libreria para las funciones relacionadas al tiempo. (time)

#set out GPIO numberring to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Definir los pines GPIO a usar.
channel =24 #Sensor de Humedad
motor = 25  #Bomba de agua
led1= 18    #Led Verde
led2 = 17   # Led Azul

#configuramos los pines GPIO como Input (entrada).
GPIO.setup(channel,GPIO.IN)
#configuramos los pines GPIO como Output (salida).
GPIO.setup(25,GPIO.OUT) #Bomba de Agua
GPIO.setup(18,GPIO.OUT) #Led Verde
GPIO.setup(17,GPIO.OUT) #Led Azul

#Funcion para obtener el valor digital.
def medirHumedad():
    valor = GPIO.input(24) #Entrada del sensor
    if valor == 0:
        print("Humedo") #Imprimir valores
        
    else:
        print("Seco") #Imprimir valores
        
    print("sensando humedad")
        
    if valor >0:
        GPIO.output(18, True) #Encender led Verde
        GPIO.output(25, True) #Encender bomba de agua
        GPIO.output(17, False) ## Apagar led azul
        print("Encendiendo bomba de agua")
        time.sleep (10)
        print("Apagando bomba de agua")
        
    elif not():
        GPIO.output(17, True) ## Encender led azul
        time.sleep(1) # Esperamos 1 segundo
        GPIO.output(17, False) ## Apagar led azul
        time.sleep(1) ## Esperamos 1 segundo
            
        GPIO.output(25, False) #Apagar bomba
        GPIO.output(18, False) #Apagar led Verde

    
    #Definir un ciclo infinito para medir la humedad cada 2 segundos.
while True:
    medirHumedad()
    time.sleep(2)