# switch button
from machine import Pin  # Class Pin ; Pin實體
import time # madule

green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
button= Pin(14, mode=Pin.PULL_DOWN) #設定GPIO14為button下拉電阻
is_press = False  #因為一開始沒人按按鈕 

while True:
    if button.value(): # button.value()=1有按下 
        is_press = True
    #elif is_press == True: # 沒按下的情況  再度按下
    elif is_press: #取代上一行  簡潔
         print("release")
         is_press = False