# switch功能 改成function  就套用到多個按鍵
from machine import Pin  # Class Pin ; Pin實體
import time # madule

green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
button= Pin(14, mode=Pin.PULL_DOWN) #設定GPIO14為button下拉電阻
is_press = False  #因為一開始沒人按按鈕 
led_status = False #led預設為暗

def btn_detect(btn1):
    global is_press, led_status #function內要再引入原本的預設值
    
    if btn1.value():  # 為True
        time.sleep_ms(50)  #20~50ms  隔了50毫秒 (避開彈跳時間) 
        if button.value():  # 為True 
            is_press = True 
    elif is_press:
        time.sleep_ms(50)  #隔了50毫秒後再測 (避開彈跳時間) 
        if btn1.value()==False: #假設過了50毫秒後有放開按鍵
            print("release")
            led_status = not led_status
            green_led.value(led_status)
            is_press = False
            
while True:
    btn_detect(button)