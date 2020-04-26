#!/usr/bin/env python3
import serial
import numpy as np
import time
# import matplotlib
# matplotlib.use("Pdf")
# import matplotlib.pyplot as plt
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

try:
    ser.open()
except:
    pass
#
# def saomiao(nmp):
#     ser.write('s'.encode())
#     ser.flushInput()
#     for i in range(0,180):
#         time.sleep(1)
#         shi = str(ser.readline())
#         shi=shi[2:len(shi)-5]
#         shi=shi.strip()
#         shi=shi.split(',')
# #         print(shi)
#         nmp[i,:]=np.array(shi)
# #         print(shi)
#         pass
#     return nmp
#     pass
# # def tu(filename,nmp):
# #     plt.figure(dpi=500)
# #     plt.imshow(nmp)
# #     plt.colorbar()
# #     plt.savefig(filename)
# #     return 'OK'
# #     pass
# def qfm():
#
#     # takephoto()
#     pass
# # def takephoto:
# #
#     pass
ser.write('q'.encode())
# ser.flushInput()
# time.sleep(5)
shi = str(ser.readline())
shi=shi[2:len(shi)-5]
