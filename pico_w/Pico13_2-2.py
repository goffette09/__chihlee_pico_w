# switch button  處理彈跳問題
from machine import Pin  # Class Pin ; Pin實體
import time # madule

green_led = Pin(15, mode=Pin.OUT) # Pin(15,Pin.OUT)亦可
button= Pin(14, mode=Pin.PULL_DOWN) #設定GPIO14為button下拉電阻
is_press = False  #因為一開始沒人按按鈕 
led_status = False #led預設為暗

while True:
    if button.value():  # 為True
        time.sleep_ms(50)  #20~50ms  隔了50毫秒 (避開彈跳時間) 
        if button.value():  # 為True 
            is_press = True 
    elif is_press:
        time.sleep_ms(50)  #隔了50毫秒後再測 (避開彈跳時間) 
        if button.value()==False: #假設過了50毫秒後有放開按鍵
            print("release")
            led_status = not led_status
            green_led.value(led_status)
            is_press = False
