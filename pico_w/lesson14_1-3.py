from machine import Timer,Pin

def fun10(t:Timer |None = None): # :Timer可省略(寫出來提醒自己); 若沒賦值的話預設為None
    print('10 seconds passed!')
    led.toggle() #toggle: 拴扣

led = Pin(15, Pin.OUT) #led實體要在fun10()之前, 因為fun10()內包含led
#fun10() #fun10()先執行一遍: 一開始亮燈10秒  
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)
fun10() #fun10()後執行一遍: 一開始熄燈10秒,就亮燈

#加入while 迴圈 執行結果稍有不同
while True:
    pass