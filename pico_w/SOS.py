import time
from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
while True:
    i=0
    for i in range(12):
        if i<3 or 7<i<11: # "S"
            led.on()
            time.sleep(0.15)
            led.off()
            time.sleep(0.15)
            i += 1
        elif 3<i<7:  #"O"
            led.on()
            time.sleep(0.7)
            led.off()
            time.sleep(0.15)
            i += 1
        elif i==3 or i==7:
            led.off()
            time.sleep(0.3)
            i += 1    
        elif i==11:
            led.off()
            time.sleep(2)