import serial
import time  ####################
ser = serial.Serial('/dev/ttyUSB0',9600)
####################
time.sleep(5)
        # set DTR line to specified logic level
ser.write('q'.encode())
print("OK")
# 接受数据
# print(ser.read())

# 发送数据
ser.write(b'\02')
ser.flush()
ser.close()
if ser.isOpen():
    ser.close()
