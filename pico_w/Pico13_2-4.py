# 參考pico11_2_4.py code
from machine import Pin  # Class Pin ; Pin實體
import time # madule
from tools import connect, reconnect
import urequests as requests


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
            try:
                if led_status ==True:
                    get_url=f'https://blynk.cloud/external/api/update?token=gg8uB11T8EXSWdrm5XJvc6sTKM5jdMPF&v0=1'
                # 從Blynk設定後取得token及網址, 亦可在Codespace安裝Thunder Client後進行控制
                else:
                    get_url=f'https://blynk.cloud/external/api/update?token=gg8uB11T8EXSWdrm5XJvc6sTKM5jdMPF&v0=0'              
                response = requests.get(get_url)    
            except: #try失敗就執行此行
                reconnect()
            else:
                if response.status_code == 200: # 200代表連線成功
                    print("傳送成功")
                else:
                    print('server有錯誤訊息')
                    print(f'status_code:{response.status_code}')
                
                response.close()
                
connect() #呼叫fuction一次                
while True:
    btn_detect(button)