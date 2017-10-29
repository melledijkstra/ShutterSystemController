import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=19200
)

ser.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

inp = 1
while 1:
    # get keyboard input
    inp = input(">> ")
    if inp == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(str.encode(inp + '\r\n'))

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)

        out = ""
        while ser.inWaiting() > 0:
            out += str(ser.read(1), 'utf-8')

        if out != '':
            print(">> " + out)