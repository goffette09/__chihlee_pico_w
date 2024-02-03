from machine import ADC,Timer
import time

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
        
start = time.ticks_ms() - 60*1000
#起始值先減60秒 使callback1裡的delta初始值為>=60*1000 這樣alert判斷式再考慮 temperature >=20

time1 =Timer()
time1.init(period=1000, callback=callback1)