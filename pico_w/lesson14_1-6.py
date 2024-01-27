from machine import Timer,Pin,ADC
import time


def fun10(t:Timer |None = None): # :Timer可省略(寫出來提醒自己); 若沒賦值的話預設為None
    print('10 seconds passed!')
    led.toggle() #toggle: 拴扣

def fun500ms(t:Timer):
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')
    
led = Pin(15, Pin.OUT) 
light = ADC(Pin(28)) # 光敏電阻的實體
vr = ADC(Pin(27)) #可變電阻的實體
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback= fun500ms)
fun10() 
