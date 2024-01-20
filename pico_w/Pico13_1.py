from machine import Pin  # Class Pin ; Pin實體
green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
green_led.value(0) # value(1)燈恆亮; value(0)不亮 
