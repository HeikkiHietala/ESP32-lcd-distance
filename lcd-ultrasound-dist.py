#This file shows the ultrasound sensor distance on an LCD. Use the other file if you want to use monitor only.
#It assumes you have an LCD that has the I2C piggyback with four connectors, VCC, GND, SDA and SCL. 

from time import sleep_ms, ticks_ms
from machine import I2C, Pin, DAC, PWM
import esp8266_i2c_lcd 
from hcsr04 import HCSR04

#sensor pins are set here
sensor = HCSR04(trigger_pin=16, echo_pin=2)
#these set up the display pins
i2c = I2C(scl=Pin(21), sda=Pin(22), freq=400000)
#at the end, the 4 is for rows, the 20 for columns, so adjust to suit your display
lcd = esp8266_i2c_lcd.I2cLcd(i2c, 0x27, 4, 20)

def main():

  while True:
    distance = sensor.distance_cm() #get the distance
    message = "Distance: " + str(int(distance)) + " cm" #prepare LCD message
    lcd.putstr(message) # show it
    time.sleep_ms(500) #wait half a second before measuring again
    lcd.clear() #clear the LCD, otherwise you get trailing characters
  
main()


