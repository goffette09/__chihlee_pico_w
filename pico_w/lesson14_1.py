from machine import Timer,Pin

def fun10(t:Timer):
    print('10 seconds passed!')

timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)
# 以上Timer 等同迴圈功能
