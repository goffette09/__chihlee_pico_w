from machine import Pin  # Class Pin ; Pin實體
import time # madule

green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
button= Pin(14, mode=Pin.PULL_DOWN) #設定GPIO14為button下拉電阻

while True:
    if button.value() == 1:
        #print("按下")
        green_led.value(1)
    else:
        green_led.value(0)
        