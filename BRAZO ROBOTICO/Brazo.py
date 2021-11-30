import RPi.GPIO as GPIO#importar libreria de las gpio del raspberry
import time#importar libreria de tiempo
GPIO.setmode(GPIO.BOARD)#mode enque se usara los pines
#definir los pines por nobres 
Led = 3
Gripper = 11
Antebrazo = 12
Brazo =13
Base = 15
#definer los pin en salida o entrada
GPIO.setup(Led, GPIO.OUT)
GPIO.setup(Base, GPIO.OUT)
GPIO.setup(Brazo, GPIO.OUT)
GPIO.setup(Antebrazo, GPIO.OUT)
GPIO.setup(Gripper, GPIO.OUT)
#crear variable para los pwm de los servos
P = GPIO.PWM(Gripper, 50)
Q = GPIO.PWM(Antebrazo, 50)
R = GPIO.PWM(Brazo, 50)
S = GPIO.PWM(Base, 50)
# valores inicializacion de los servos
P.start(5)
Q.start(5)
R.start(5)
S.start(5)
#posicion inicial de los servos
S.ChangeDutyCycle(2.5)
R.ChangeDutyCycle(2.5)
Q.ChangeDutyCycle(2.5)
P.ChangeDutyCycle(12)

GPIO.output(Led, GPIO.HIGH)#ensender led
time.sleep(3)
for i in range(0,50,1):#avanse del brazo
    DC=1./18.*(i)+2
    R.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(0,90,1):#avanse del antebrazo
    DC=1./18.*(i)+2
    Q.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(180,90,-1):#cerrar gripper
    DC=1./18.*(i)+2
    P.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(90,45,-1):#subir antebrazo
    DC=1./18.*(i)+2
    Q.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(0,180,1):#avansa dela base
    DC=1./18.*(i)+2
    S.ChangeDutyCycle(DC)
    time.sleep(0.005)
time.sleep(1)
for i in range(45,90,1):#bajar antebrazo
    DC=1./18.*(i)+2
    Q.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(90,180,1):#abrir gripper
    DC=1./18.*(i)+2
    P.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(90,0,-1):#regresar antebrazo
    DC=1./18.*(i)+2
    Q.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(45,0,-1):#regresar brazo
    DC=1./18.*(i)+2
    R.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(180,90,1):#cerrar gripper
    DC=1./18.*(i)+2
    P.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
for i in range(180,0,-1):#regresar base
    DC=1./18.*(i)+2
    S.ChangeDutyCycle(DC)
    time.sleep(0.008)
time.sleep(1)
GPIO.output(Led, GPIO.LOW)#apagar led
#detener los pwm de los servos
P.stop()
Q.stop()
R.stop()
S.stop()
GPIO.cleanup()#limpiar los datos delos puertos