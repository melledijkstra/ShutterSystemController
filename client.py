import time
import serial
import threading

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=19200
)


def read():
    while True:
        out = ""
        while ser.inWaiting() > 0:
            out += str(ser.read(ser.inWaiting()), 'utf-8')

        if out != "":
            print(out, end='')


threading.Thread(target=read).start()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

while 1:
    # get keyboard input
    print("Provide ID")
    id = input(">> ")
    print("Provide Value")
    value = input(">> ")

    if id == 'exit' or value == 'exit':
        ser.close()
        exit()
    else:
        try:
            ser.write(bytes([int(id)]))
            ser.write(bytes([int(value)]))
        except Exception as e:
            print("something went wrong 0.0")
