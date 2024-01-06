import network
import time
from machine import WDT,Timer,ADC,RTC  
import urequests as requests
import rp2

rp2.country('TW')

ssid = 'Chih Galaxy A33 5G'
password = 'enns6294'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
wlan.config(pm=0xa11140) #預設是省電模式,可改為非省電模式

def connect():

    max_wait = 10

    #處理正在連線
    while max_wait > 0:
        max_wait -= 1
        status = wlan.status()
        if status < 0 or status >=3:
            break
        print("等待連線")
        time.sleep(1) # 主機板暫停一秒不做事   這個迴圈共最多耗時10秒

    #沒有wifi的處理
    if wlan.status() != 3:
        #連線失敗,重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError('連線失敗')
    else:
        print("成功連線")
        print(wlan.ifconfig())

def reconnect():
    if wlan.status == 3:
        print(f'無法連線({wlan.status()})')
        return
    else:
        print('嘗試重新連線')
        wlan.disconnect()
        wlan.connect(ssid, password)
        connect()
    
    