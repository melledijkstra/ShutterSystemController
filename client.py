import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=19200
)

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
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(bytes([int(id)]))
        ser.write(bytes([int(value)]))

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(0.5)

        out = ""
        while ser.inWaiting() > 0:
            out += str(ser.read(1), 'utf-8')

        if out != '':
            print(">> " + out)

        time.sleep(0.5)