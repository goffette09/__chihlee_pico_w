# 加入pico10_1.py的code (溫度sensor)
import network
import time
from machine import WDT,Timer,ADC #加入ADC(類比轉數位)功能 

def connect():
    # enable station interface and connect to WiFi access point
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect('Chih Galaxy A33 5G','enns6294')

    max_wait = 10

    #處理正在連線
    while max_wait > 0:
        max_wait -= 1
        status = nic.status()
        if status < 0 or status >=3:
            break
        print("等待連線")
        time.sleep(1) # 主機板暫停一秒不做事   這個迴圈共最多耗時10秒

    #沒有wifi的處理
    if nic.status() != 3:
        #連線失敗,重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError('連線失敗')

    else:
        print("成功連線")
        print(nic.ifconfig())



def alert():
    print("要爆炸了!!!")

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
    
    # 溫度超過20度且發送alert的時間已超過60秒才執行
    if temperature >=23.5 and delta >= 60*1000: 
        alert()
        start = time.ticks_ms()

connect() #呼叫fuction一次

start = time.ticks_ms() - 60*1000
#起始值先減60秒 使callback1裡的delta初始值為>=60*1000 這樣alert判斷式再考慮 temperature >=20
time1 =Timer()
time1.init(period=1000, callback=callback1)
