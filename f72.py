#!/usr/bin/env python3
import serial
import os
import time
import csv
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
try:
    ser.open()
except:
    pass
try:
    ser.write('q'.encode())
    # print(ser.readlines())
    ser.flushInput()
