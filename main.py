from machine import I2C,Pin
import _thread,json,time
i2c=I2C(sda=Pin(5), scl=Pin(4), freq=40000000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c) 

# def tu(a,b,c):
#     oled.fill(0)
#     oled.text(a,2,2,1)
#     oled.text(b,2,12,1)
#     oled.text(c,2,22,1)
#     oled.show()

def tu(a,b,c,d,e):
    abc={}
    abc['a']=a;
    abc['b']=b;
    abc['c']=c;
    abc['d']=d;
    abc['e']=e;
    q=open("cpu.json","w")    
    q.write(json.dumps(abc))
    q.close()
# bad apple

def image(img_list):   
    s=time.ticks_ms()  
    with open("cpu.json","r") as f:
        qq=f.read()
    abc=json.loads(qq)
    oled.fill(0)     
    oled.text(abc['a'],2,2,1)
    oled.text(abc['b'],2,12,1)
    oled.text(abc['c'],2,22,1)
    oled.text('BiliBili',64,32,1)
    oled.text(abc['d'],64,40,1)
    oled.text(abc['e'],64,48,1)
    for i in img_list:
        oled.hline(i[0],i[1]+32,i[2],1)
    oled.show()
    e=time.ticks_ms()-s
    if e<100:
        time.sleep_ms(90-e)

def ot(a):
    while 1:
        with open('bad.data','r') as f:
            for i in f:
                z=json.loads(i)
                image(z)
_thread.start_new_thread(ot,('a',))