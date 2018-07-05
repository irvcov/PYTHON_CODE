
import serial

ser = serial.Serial(
    port='COM1',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
line = []

while True:
    line = ser.readline()

    if len(line) != 0:
        print line        
    # for c in ser.read():
        # line.append(c)
        # if c == '\n':
            # print("Line: " + line)
            # line = []
            # break

ser.close()
        
# print ser.read(ser.inWaiting())

# ser.close()