from machine import Timer,Pin,ADC
import time

def fun10(t:Timer |None = None): # :Timer可省略(寫出來提醒自己); 若沒賦值的話預設為None
    print('10 seconds passed!')
    led.toggle() #toggle: 拴扣

def fun500ms(t:Timer):
    print(light.read_u16())
    
led = Pin(15, Pin.OUT) #led(Pin的實體)要在fun10()之前, 因為fun10()內包含led
light = ADC(Pin(28)) #ADC的實體
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback= fun500ms)
fun10() #fun10()後執行一遍: 一開始熄燈10秒,就亮燈
