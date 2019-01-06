from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
while True:
    
    temp = sense.get_temperature()
    print(temp)
    temp = temp-10
    
    temp_str = "%10.2f Celsius" % temp
    sense.show_message(temp_str,scroll_speed = 0.07,text_colour=[0, 255, 0])
    sleep(10)