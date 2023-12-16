import time
from machine import Pin

led = Pin("LED", Pin.OUT)
while True:
    print("Light on!")
    led.high()
    time.sleep(1)
    print("Light off!")
    led.low()
    time.sleep(3)
