# ESP32-lcd-distance
This repository contains all you need to have a distance sensor's reading shown on an LCD display. 

I am using an ESP32 DevKitC and this code works with it.  

I have used dhylands' python_lcd library and the micropython-hcsr04 from rsc1975.

See my blog at www.sabulo.com for all my projects with Arduino, ESP32, 3D modeling with Blender, and 3D printing with a variety of machines.

FILES:

1) To run any distance measurement, you need the hcsr04.py 

2) To add LCD, you need 
    
    esp32_gpio_lcd.py
    esp8266_i2c_lcd.py
    lcd_api.py
    
    on the chip.

3) To add connectivity to website and JSON capabilities, you need
 
    urequests.py

4) To get your device to start the program you want as it boots, you need to edit 

    boot.py
