import smbus
import time

# Set up I2C communication
bus = smbus.SMBus(1)
QMC5883L_ADDR = 0x0D

def read_compass():
    data = bus.read_i2c_block_data(QMC5883L_ADDR, 0x00, 6)
    x = data[0] | (data[1] << 8)
    y = data[2] | (data[3] << 8)
    z = data[4] | (data[5] << 8)
    
    # Convert to signed 16-bit values
    if x >= 32768: x -= 65536
    if y >= 32768: y -= 65536
    if z >= 32768: z -= 65536

    return x, y, z

while True:
    x, y, z = read_compass()
    print(f"Compass Data - X: {x}, Y: {y}, Z: {z}")
    time.sleep(1)
