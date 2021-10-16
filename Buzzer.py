from gpiozero import Buzzer
from time import sleep
buzzer=Buzzer(4) #gpio 4
buzzer.on()
sleep(3)
buzzer.off()
