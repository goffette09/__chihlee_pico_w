import network
import time

ssid='Chih Galaxy A33 5G'
password ='enns6294'

wlan = network.WLAN(network.STA_IF) # 命名wlan為一實體, 執行實體方法(network.STA_IF)
wlan.active(True)  # 執行實體方法()
wlan.disconnect()   #加上這行 可看到互動環境起先顯示"等待連線"
wlan.connect(ssid,password) # ()
#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#status<0, >3 :失敗的連線

max_wait = 10
while max_wait > 0:  #至多執行10次
    status = wlan.status()
    if status<0 or status >=3:
        break
    max_wait -= 1
    print("等待連線")
    time.sleep(1) 

# 檢查目前連線狀態

if wlan.status() !=3:
    raise RuntimeError('連線失敗') # raise丟出錯誤  crash

else:
    print('連線成功')
    configure = wlan.ifconfig()
    print(f'ip={configure[0]}')
