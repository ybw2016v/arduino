
import serial

ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
ser.write('q'.encode())
# ser.flushInput()
# time.sleep(5)
# shi = str(ser.readline())
# shi=shi[2:len(shi)-5]
