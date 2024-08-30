import serial
import pynmea2

port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=1)

while True:
    try:
        line = ser.readline().decode('ascii', errors='replace')
        if line.startswith('$GPGGA'):
            msg = pynmea2.parse(line)
            print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")
    except pynmea2.ParseError as e:
        print(f"Parse error: {e}")
        continue
