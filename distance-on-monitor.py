#This file shows the ultrasound sensor distance on monitor only. Use the other file if you want to use an LCD.

from time import sleep_ms, ticks_ms
from machine import I2C, Pin, DAC, PWM
from hcsr04 import HCSR04 #the driver for the ultrasound 

#the following set assumes you have five sensors, edit to suit your setup
sensorA = HCSR04(trigger_pin = 12, echo_pin = 4)
sensorB = HCSR04(trigger_pin = 14, echo_pin = 16)
sensorC = HCSR04(trigger_pin = 27, echo_pin = 17)
sensorD = HCSR04(trigger_pin = 26, echo_pin = 5)
sensorE = HCSR04(trigger_pin = 25, echo_pin = 18)


message=""

def main():
  while True:

    distanceA = sensorA.distance_cm()
    distanceB = sensorB.distance_cm()
    distanceC = sensorC.distance_cm()
    distanceD = sensorD.distance_cm()
    distanceE = sensorE.distance_cm()
    
    message = "A" + str(int(distanceA)) + " B" + str(int(distanceB)) + " C" + str(int(distanceC)) + " D" + str(int(distanceD)) + " E" + str(int(distanceE))
    print(message) #prints the result on the monitor
    sleep_ms(1000)
  
main()
