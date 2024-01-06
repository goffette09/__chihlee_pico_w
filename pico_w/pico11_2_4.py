# 解決 get方法會有連不上網路的情況 (用 try except架構解決)
from tools import connect, reconnect
from machine import WDT,Timer,ADC,RTC  
import urequests as requests


def alert(t:float):
    print("要爆炸了!!!")
    rtc = RTC()
    date_tuple = rtc.datetime()
    year = date_tuple[0]
    month = date_tuple[1]
    day = date_tuple[2]
    hour = date_tuple[4]
    minutes = date_tuple[5]
    second = date_tuple[6]
    date_str = f'{year}-{month}-{day} {hour}:{minutes}:{second}'
    
    #解決 get方法會有連不上網路的情況 (用 try except架構解決)
    try:
        response = requests.get(f'https://hook.eu2.make.com/vubx782mcs9ycvz2ww8h9t9rpnqfvqvf?name=pico_我家冰箱&date={date_str}&temperature={t}')    
    except: #try失敗就執行此行
        reconnect()
    else:
        if response.status_code == 200: # 200代表連線成功
            print("傳送成功")
        else:
            print('server有錯誤訊息')
            print(f'status_code:{response.status_code}')
        response.close()
    
def callback1(t:Timer):
    global start # 指定外部的start進來
    sensor = ADC(4) # the 5th pin sense temperature (0~4)
    #print(temperature.read_u16())
    vol = sensor.read_u16()*3.3/65535
    temperature = 27 - (vol-0.706)/0.001721
    #print(start)#temperature)#vol)
    print(f'溫度:{temperature}')
    delta = time.ticks_diff(time.ticks_ms(), start) 
    print(delta)
    
    # 溫度超過20.5度且發送alert的時間已超過60秒才執行
    if temperature >=20.5 and delta >= 60*1000: 
        alert(temperature)
        start = time.ticks_ms()

connect() #呼叫fuction一次

start = time.ticks_ms() - 60*1000
#起始值先減60秒 使callback1裡的delta初始值為>=60*1000 這樣alert判斷式再考慮 temperature >=20
time1 =Timer()
time1.init(period=1000, callback=callback1)

