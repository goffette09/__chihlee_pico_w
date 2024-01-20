from machine import Pin  # Class Pin ; Pin實體
green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
green_led.value(0)
