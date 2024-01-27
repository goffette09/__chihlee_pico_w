#加入連線功能 (blynk 和pico-W之間連線)
import Timer,Pin,ADC
import time
from tools import connect,reconnect  #Pico有tools 程式
import urequests as requests

def fun10(t:Timer |None = None):
    light_value = light.read_u16()
    vr_value = vr.read_u16()
    url = f'https://blynk.cloud/external/api/batch/update?token=gg8uB11T8EXSWdrm5XJvc6sTKM5jdMPF&v0={light_value}&v1={vr_value}'
    
    #使用try...except架構解決連線失敗問題(失敗就重連) 
    try:
        led.value(1) #連成就亮燈
        response = requests.get(url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print('傳送成功')
        else:
            print('傳送失敗')
        response.close()
    led.value(0) #執行完 就關燈

def fun500ms(t:Timer): 
    print(f'light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')

connect() #先連線
led = Pin(15, Pin.OUT) #(已先接GIPO15)
light = ADC(Pin(28)) # 光敏電阻的實體(已先接GIPO28 ADCport)
vr = ADC(Pin(27)) #可變電阻的實體(已先接GIPO27 ADCport)
timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback= fun10)
#每隔10秒就執行一次fun10, 即會連線到Blynk+變換LED開關 (Blynk上會顯示兩電阻數值)
timer500ms = Timer(period=500, mode=Timer.PERIODIC, callback= fun500ms)
#每隔0.5秒就執行一次fun500ms, 即會顯示一次光敏電阻、可變電阻數值
fun10() 
