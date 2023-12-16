from machine import Timer

def callback1(t:Timer):
    print(1)
    
def callback2(t:Timer):
    print(2)
def callback3(t:Timer):
    print(3)
    t.deinit()
    
timer1 = Timer()
timer1.init(freq=1,callback=callback1)

timer2 = Timer()
timer2.init(period=2000,callback=callback2)

timer3 = Timer()
timer3.init(period=3000, callback=callback3)