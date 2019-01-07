#!/usr/bin/python
from sense_hat import SenseHat
import time

ap = SenseHat()
ho = ap.get_temperature()
ho = ho-10.5
par = ap.get_humidity()
leg = ap.get_pressure()


#print("Homerseklet: %s C" % temp)               # Homerseklet konzolon kiirasa
#print("Paratartalom: %s %%rH" % humidity)        # Paratartalom konzolon kiirasa
#print("Legnyomas: %s Millibars" % pressure)    # Legnyomas konzolon kiirasa

ap.set_rotation(180)        # LED matrix jobbrol balra forgatasa
              
ap.show_message("%.1f C" % ho, scroll_speed=0.10, text_colour=[0, 255, 0])

time.sleep(1)           # 1s varakozas

ap.show_message("%.1f %%rH" % leg, scroll_speed=0.10, text_colour=[255, 0, 0]) 

time.sleep(1)      # 1s varakozas

ap.show_message("%.1f Millibars" % par, scroll_speed=0.10, text_colour=[0, 0, 255])

ap.clear()      # LEDek kikapcsolasa