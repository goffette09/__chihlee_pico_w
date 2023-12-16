from machine import ADC,Timer

def callback1(t:Timer):
    sensor = ADC(4) # the 5th pin (0~4)
    #print(temperature.read_u16())
    vol = sensor.read_u16()*3.3/65535
    temperature = 27 - (vol-0.706)/0.001721
    print(temperature)#vol) 
time1 =Timer()
time1.init(period=1000, callback=callback1)