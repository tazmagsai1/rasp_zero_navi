import smbus
import serial
import time

# Set up I2C and Serial communication
bus = smbus.SMBus(1)
QMC5883L_ADDR = 0x0D
gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
ultrasonic_sensor = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

def read_compass():
    data = bus.read_i2c_block_data(QMC5883L_ADDR, 0x00, 6)
    x = data[0] | (data[1] << 8)
    y = data[2] | (data[3] << 8)
    z = data[4] | (data[5] << 8)
    
    if x >= 32768: x -= 65536
    if y >= 32768: y -= 65536
    if z >= 32768: z -= 65536
    
    return x, y, z

def read_gps():
    try:
        data = gps.readline().decode('ascii', errors='replace')
        if data.startswith('$GPGGA'):
            return data
    except:
        return None

def read_ultrasonic():
    try:
        data = ultrasonic_sensor.readline().decode('ascii', errors='replace')
        return data
    except:
        return None

while True:
    compass_data = read_compass()
    gps_data = read_gps()
    ultrasonic_data = read_ultrasonic()

    # Combine the data for processing
    print(f"Compass: {compass_data}, GPS: {gps_data}, Ultrasonic: {ultrasonic_data}")
    time.sleep(1)
