import serial
import time

# Set up Serial communication
gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

def read_gps():
    if gps.in_waiting > 0:  # Check if there is data waiting to be read
        try:
            data = gps.readline().decode('ascii', errors='replace')
            if data:
                print(f"Raw GPS Data: {data}")  # Print all incoming data
                if data.startswith('$GPGGA'):
                    print(f"GPS Data: {data}")
        except Exception as e:
            print(f"Error: {e}")

while True:
    read_gps()
    time.sleep(1)
