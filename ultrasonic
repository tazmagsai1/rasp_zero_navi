import serial
import time

# Set up Serial communication
ultrasonic_sensor = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

def read_ultrasonic():
    try:
        data = ultrasonic_sensor.readline().decode('ascii', errors='replace')
        print(f"Ultrasonic Sensor Data: {data}")
    except Exception as e:
        print(f"Error: {e}")

while True:
    read_ultrasonic()
    time.sleep(1)
