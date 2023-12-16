print("Hello Pico!")


import time
from machine import Pin

led = Pin("LED", Pin.OUT)
while True:
    print("Light on!")
    led.on()
    time.sleep(3)
    print("Light off!")
    led.off()
    time.sleep(3)