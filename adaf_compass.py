import board
import busio
import adafruit_qmc5883l

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the QMC5883L sensor
sensor = adafruit_qmc5883l.QMC5883L(i2c)

while True:
    # Read magnetometer data
    mag_x, mag_y, mag_z = sensor.magnetic
    print(f"Magnetometer X: {mag_x}, Y: {mag_y}, Z: {mag_z}")
