import smbus
import time

# Set up I2C communication
bus = smbus.SMBus(1)
QMC5883L_ADDR = 0x43  # Replace with your device's I2C address

# Initialize the QMC5883L
def init_compass():
    bus.write_byte_data(QMC5883L_ADDR, 0x0B, 0x01)  # Set to continuous mode
    bus.write_byte_data(QMC5883L_ADDR, 0x09, 0x00)  # Set to 200Hz data rate

def read_raw_data():
    try:
        # Attempt to read 6 bytes from the sensor's data registers
        data = bus.read_i2c_block_data(QMC5883L_ADDR, 0x00, 6)
        return data
    except Exception as e:
        print(f"Error reading compass: {e}")
        return None

# Initialize the compass
init_compass()

while True:
    raw_data = read_raw_data()
    if raw_data:
        # Convert the raw data to signed integers
        x = (raw_data[0] << 8) | raw_data[1]
        y = (raw_data[2] << 8) | raw_data[3]
        z = (raw_data[4] << 8) | raw_data[5]

        # Handle signed values
        if x >= 32768:
            x -= 65536
        if y >= 32768:
            y -= 65536
        if z >= 32768:
            z -= 65536

        print(f"Compass Data - X: {x}, Y: {y}, Z: {z}")
    else:
        print("Failed to read from compass.")
    time.sleep(1)
