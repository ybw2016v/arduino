#!/usr/bin/env python3
import serial
import numpy as np
import os
import time

class ard(object):
    # self.ser=serial.Serial('/dev/ttyUSB0', 9600)

    def __init__(self):
        self.ser=serial.Serial('/dev/ttyUSB0', 9600)
        sser=self.ser
        # sser.open()
        try:
            sser.open()
        except:
            # print("W")
            pass
    def saomiao(self,nmp):
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
        return nmp
        pass
    def qfm(self):
        sser=self.ser
        sser.write(b'q')
        sser.flushInput()
        print("dog")
        # time.sleep(5)
        shi = str(sser.readline())
        shi=shi[2:len(shi)-5]
        print(shi)
        self.takephoto()
        pass
    def takephoto(self):
        timedog=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        str = os.popen("echo takephoto"+timedog).read()
        print(str)
        pass

    pass
