# pico11_1.py僅能執行一次, 此處示範改成function得以重複執行 (即connect)

import network
import time
from machine import WDT,Timer

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

def mycallback(t:Timer):
    print("Hello World")
    t.deinit()  #執行一次就消滅  關掉此行則會每秒print一次

connect() #呼叫fuction一次
tim = Timer()
tim.init(period=1000, callback=mycallback) #period=1000(毫秒) =1秒 每隔一秒做一次
#while True:
#    time.sleep(1) #主機板暫停一秒不做事
