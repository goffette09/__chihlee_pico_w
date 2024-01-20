from machine import Pin  # Class Pin ; Pin實體
import time # madule

green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
button= Pin(14, mode=Pin.PULL_DOWN) #設定GPIO14為button下拉電阻
is_press = False  #因為一開始沒人按按鈕 
 
while True:
    if button.value():
        is_press = True
    else: # 沒按下的情況
        if is_press == True: #再度按下
            print("release")
            is_press = False