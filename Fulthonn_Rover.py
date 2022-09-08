import RPi.GPIO as GPIO                    #Importation de la librairie GPIO library
import time

#Importation de la librarie time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 17
ECHO = 27
led = 22

moteur1=16
moteur2=12
moteur3=21
moteur4=20

GPIO.setup(TRIG,GPIO.OUT)                  # initialisation de GPIO Pin en tant que outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialisation de GPIO comme Pin input
GPIO.setup(led,GPIO.OUT)                  

GPIO.setup(moteur1,GPIO.OUT)
GPIO.setup(moteur2,GPIO.OUT)
GPIO.setup(moteur3,GPIO.OUT)
GPIO.setup(moteur4,GPIO.OUT)

GPIO.output(led, 1)

time.sleep(5)


def left():
    GPIO.output(moteur1, 0)
    GPIO.output(moteur2, 0)
    GPIO.output(moteur3, 1)
    GPIO.output(moteur4, 0)
    print ("Tourner à gauche")

def right():
    GPIO.output(moteur1, 1)
    GPIO.output(moteur2, 0)
    GPIO.output(moteur3, 0)
    GPIO.output(moteur4, 0)
    print ("Trourner à droite")


def back():
    GPIO.output(moteur1, 0)
    GPIO.output(moteur2, 1)
    GPIO.output(moteur3, 0)
    GPIO.output(moteur4, 1)
    print ("marche arrière")


def stop():
    print ("stop")
    GPIO.output(moteur1, 0)
    GPIO.output(moteur2, 0)
    GPIO.output(moteur3, 0)
    GPIO.output(moteur4, 0)

def forward():
    GPIO.output(moteur1, 1)
    GPIO.output(moteur2, 0)
    GPIO.output(moteur3, 1)
    GPIO.output(moteur4, 0)
    print ("Forward")

bienvenue="#### Fulthonn Robotic Laboratory ####\n"
for letter in bienvenue:
    print(letter,end=" ")
    time.sleep(0.09)
print("\n")   
project="    ~~~~Département de IA~~~~~\n "    
for letter in project:
    print(letter,end=" ")
    time.sleep(0.09)
print("")

project="@@ Centre des voitures intelligentes @@\n"    
for letter in project:
    print(letter,end=" ")
    time.sleep(0.09)
print("")
 

print("Lancement dans ...")
time.sleep(0.5)

project="5 4 3 2 1 0 \n"    
for letter in project:
    print(letter,end=" ")
    time.sleep(1)
print("")

time.sleep(0.5)

stop()
count=0
while True:
 i=0
 DistanceMoyenne=0
 for i in range(5):
  GPIO.output(TRIG, False)                 # config de l'envoi des impulsion au niveau bas
  time.sleep(0.1)                      #suspendre pour 1/10 de seconde

  GPIO.output(TRIG, True)                  #config de lenvoir au niveau haut
  time.sleep(0.00001)                           #attendre 1/100000 de seconde
  GPIO.output(TRIG, False)                 #config de l'envoi des impulsion au niveau bas

  while GPIO.input(ECHO)==0:              # verifier si l'envoie est au niveau bas
       GPIO.output(led, False)             
  debutDePulsation = time.time()

  while GPIO.input(ECHO)==1:              #verifier si l'envoie est au niveau haut
       GPIO.output(led, False) 
  finDePulsation = time.time()
  pulse_duration = finDePulsation - debutDePulsation #optension de la durée de la pulsation

  distance = pulse_duration * 17150        #multiplication des la duré par 17150 pour obtenir la distance
  distance = round(distance,2)                 #arondir à 2 chiffre après la virgule
  DistanceMoyenne=DistanceMoyenne+distance

 DistanceMoyenne=DistanceMoyenne/5
 print (DistanceMoyenne)
 flag=0
 if DistanceMoyenne < 45:
    count=count+1
    stop()
    time.sleep(0.5)
    back()
    time.sleep(0.5)
    if (count%3 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
    time.sleep(0.5)
    stop()
    time.sleep(0.5)
 else:
    forward()
    flag=0

