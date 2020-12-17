import psutil
import serial
import time
import requests



uid="1369152"
ser=serial.Serial("com3",115200,timeout=0.5)
def x(cv):
    if cv<1024*1024*1024:
        return str(cv//(1024*1024))+"MB"
    else:
        return str(round(cv/(1024*1024*1024)))+"GB"



while True:
    url="http://api.bilibili.com/x/relation/stat?vmid="+uid
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE' }
    re=requests.get(url,headers=headers)
    my=re.json()
    if my['code']==0:
        e= my['data']['follower']
    else:
        e=0
    tm=time.localtime()
    f=str(tm.tm_hour)+':'+str(tm.tm_min)
    a=psutil.cpu_count()
    b=psutil.cpu_percent()
    c=psutil.virtual_memory()
    # svmem(total=8071716864, available=6532554752, percent=19.1, used=1258717184, free=6526308352, active=1153519616, inactive=194592768, buffers=2129920, cached=284561408, shared=9011200, slab=39006208)
    d=psutil.disk_usage('c://')
    # sdiskusage(total=85857402880, used=3858100224, free=81999302656, percent=4.5)

    while b==0:
        b=psutil.cpu_percent()

    aa=str(a)+" CPU "+str(b)+"%"
    bb=x(c.total)+" Mem  "+str(c.percent)+"%"
    cc="C: "+x(d.total)+" "+str(d.percent)+"%"
    time.sleep(1)
    print(aa,bb,cc)
    q="tu('%s','%s','%s','%s','%s')\r" % (aa,bb,cc,e,f)
    print(q)
    ser.write(q.encode())
