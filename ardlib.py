#!/usr/bin/env python3
import serial
import numpy as np
import os
import time
import datetime
import shutil
import matplotlib
matplotlib.use("Pdf")
import matplotlib.pyplot as plt

class ard(object):
    # self.ser=serial.Serial('/dev/ttyUSB0', 9600)

    def __init__(self):
        self.ser=serial.Serial('/dev/ttyUSB0', 9600)
        time.sleep(1)
        sser=self.ser
        # sser.open()
        try:
            sser.open()
        except:
            # print("W")
            pass
    def saomiao(self):
        nmp=np.zeros([180,180])
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))


        sser=self.ser
        sser.write('s'.encode())
        sser.flushInput()
        for i in range(0,180):
            time.sleep(1)
            shi = str(sser.readline())
            shi=shi[2:len(shi)-5]
            shi=shi.strip()
            shi=shi.split(',')
            nmp[i,:]=np.array(shi)
            pass


        p=os.path.abspath('.')
        ba=os.popen('mkdir '+p+'/static/res2/'+self.nowTime)
        time.sleep(0.001)


        # print(p)
        # p2=os.path.join(p,'/static/res2/'+self.nowTime+r'/res2.html')
        # os.mkdir(os.path.join(p,'/static/res1/'+self.nowTime))
        # b=os.popen('mkdir '+p+'/static/res2/'+self.nowTime)
        plt.figure(dpi=500)
        plt.imshow(nmp)
        plt.title('space')
        plt.colorbar()
        plt.savefig('data.jpg')


        # os.mkdir(os.path.join(p,'/static/res1/'+self.nowTime))
        b=os.popen('cp data.jpg '+p+'/static/res2/'+self.nowTime)
        shutil.copyfile('./static/res2.html','./static/res2/'+self.nowTime+r'/res.html')

        # return nmp

    def qfm(self):
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        sser=self.ser
        time.sleep(1)
        sser.write(b'q')
        # sser.flushInput()
        print("dog")
        # time.sleep(5)
        # shi = str(sser.readline())
        # shi2= str(sser.readline())
        # shi=shi2[2:len(shi)-5]
        # print(shi)
        self.takephoto()
        p=os.path.abspath('.')
        print(p)
        p2=os.path.join(p,'/static/res1/'+self.nowTime+r'/res1.html')
        # os.mkdir(os.path.join(p,'/static/res1/'+self.nowTime))
        b=os.popen('mkdir '+p+'/static/res1/'+self.nowTime)
        time.sleep(0.001)
        a=os.popen('touch '+p+p2)
        print(b)
        print(a)
        print(p+p2)
        with open(p+p2,'w') as f:
            f.write('dog\n'+self.nowTime)
            shutil.copyfile('./static/res1.html','./static/res1/'+self.nowTime+r'/res.html')
        # return shi
        # pass
    def takephoto(self):
        timedog=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        str = os.popen("echo takephoto"+timedog).read()
        print(str)
        pass
    def test(self):
        print("OK")
        pass

    pass
