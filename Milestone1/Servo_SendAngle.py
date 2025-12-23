import serial
import time

PORT = "/dev/cu.usbserial-1420"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

def move_servo(angle):
    str_angle = f'{angle}\n'
    ser.write(str_angle.encode())

try:
    while True:
        angle = input("Input sudut gerakan: ")
        move_servo(angle)
        time.sleep(2)

except KeyboardInterrupt:
    print("Keluar ...")
finally:
    ser.close()