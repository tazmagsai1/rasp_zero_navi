import serial
import time

# Set up Serial communication
gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

def read_gps():
    try:
        data = gps.readline().decode('ascii', errors='replace')
        if data.startswith('$GPGGA'):  # Typical NMEA sentence
            print(f"GPS Data: {data}")
    except Exception as e:
        print(f"Error: {e}")

while True:
    read_gps()
    time.sleep(1)
