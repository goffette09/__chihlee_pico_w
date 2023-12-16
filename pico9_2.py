from machine import Timer

def callback1(t):
    print(1)
    
def callback2(t):
    print(2)

timer1 = Timer()
timer1.init(freq=1,callback=callback1)

timer2 = Timer()
timer2.init(period=2000,callback=callback2)