#!/usr/bin/env python3
import serial
import os
import time
import csv
import datadog
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
try:
	ser.open()
except:
	pass
try:
    ser.write('r'.encode())
    # print(ser.readlines())
    ser.flushInput()
    i=0
    while 1:
        ser.write('r'.encode())
        shi = str(ser.readline())
        wen = str(ser.readline())
        zhuangtai = str(ser.readline())
        if len(shi)>=4:
            timedog=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            datas=[timedog,shi[2:len(shi)-5],wen[2:len(wen)-5],zhuangtai[2:len(zhuangtai)-5]]
            with open('data.csv','a+') as filed:
                csv_write=csv.writer(filed)
                csv_write.writerow(datas)
            with open('now.txt','w') as nowf:
                strdog='Humidity (%):'+shi[2:len(shi)-5]+'Temperature (oC):'+wen[2:len(wen)-5]
                nowf.write(strdog)
            # print('OK')
        ser.flushInput()
        # filed.save()
        time.sleep(30)
        if i>=1 :
            datadog.update_and_plot('data.csv')
        i=i+1
except KeyboardInterrupt:
    ser.close()
