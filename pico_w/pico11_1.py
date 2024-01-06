# class WLAN – control built-in WiFi interfaces
# copy code from: "https://docs.micropython.org/en/latest/library/network.WLAN.html
import network
import time
# enable station interface and connect to WiFi access point

from machine import WDT


nic = network.WLAN(network.STA_IF)  # 命名nic為一實體, 執行實體方法WLAN(network.STA_IF)
nic.active(True) # 實體方法WLAN.active()
nic.connect('Chih Galaxy A33 5G','enns6294') # 實體方法WLAN.connect()
#nic.connect('your-ssid', 'your-key')
# now use sockets as usual

#if nic.isconnected():
#    print("連線成功!")
#else:
#    print("連線失敗!")
# isconnected()不知嘗試連線幾次，僅回傳連線成功與否→改用WLAN.status()

#WLAN.status()
#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#status<0, >3 :失敗的連線

max_wait = 10

#處理正在連線
while max_wait > 0:
    max_wait -= 1  #隨執行一次 max_wait每次遞減一
    
    status = nic.status()
    if status < 0 or status >= 3:
        break  #非status定義下的錯誤狀態，就跳出迴圈
    print("等待連線")
    time.sleep(1) #將下面while迴圈的time.sleep(1)移到這個迴圈
    
# 設定: not wlan.isconnected() and wlan.status()>=0 代表尚未連線的錯誤狀態
#while not nic.isconnected() and nic.status() >=0: #尚未連線則執行以下步驟
#    print("等待連線")
    #time.sleep(1)
#以上三行是 沒有限制次數的迴圈

#print("有可能沒有WIFI主機")
#print("已經連線成功")

# 沒有wifi的處理
if nic.status() !=3:
    #連線失敗, 重新開機
    #pass
    #參考老師repo的:pico_W/一般操作/0_3重新啟動(WTD)/  先在上方加入:from machine import WDT
    #以下兩行會重開機  在開發階段先以註解關閉功能  改用raise RuntimeError('連線失敗')
    #wdt = WDT(timeout=2000)
    #wdt.feed()
    raise RuntimeError('連線失敗')  #raise丟出錯誤

else:
    print('成功連線')
    print(nic.ifconfig()) #將原本簡單結構的print(nic.ifconfig())移到迴圈內


#print(nic.ifconfig()) #顯示IP位置
    