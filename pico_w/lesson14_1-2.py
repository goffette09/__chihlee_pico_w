from machine import Timer,Pin

def fun10(t:Timer |None = None): # :Timer可省略(寫出來提醒自己); 若沒賦值的話預設為None
    print('10 seconds passed!')
    
fun10()  #fun10()先執行一遍
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)

#加入while 迴圈 執行結果稍有不同
while True:
    pass