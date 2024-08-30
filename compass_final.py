import smbus
import time

# I2C address of the sensor
QMC5883L_ADDR = 0x1e  # Change this to 0x1e based on your i2cdetect result

# Initialize I2C (SMBus)
bus = smbus.SMBus(1)

def read_raw_data(addr):
    # Read data from given address
    high = bus.read_byte_data(QMC5883L_ADDR, addr)
    low = bus.read_byte_data(QMC5883L_ADDR, addr + 1)
    value = (high << 8) + low
    if value > 32767:
        value -= 65536
    return value

def read_compass():
    x = read_raw_data(0x00)
    y = read_raw_data(0x02)
    z = read_raw_data(0x04)
    return x, y, z

while True:
    x, y, z = read_compass()
    print(f"X: {x}, Y: {y}, Z: {z}")
    time.sleep(1)
