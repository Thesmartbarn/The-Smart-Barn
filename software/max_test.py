import board
import digitalio
import adafruit_max31865
import time

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs,wires =4,rtd_nominal=100.0,ref_resistor=4300.0)

while True:
    # Read temperature.
    temp = sensor.temperature
    res = sensor.resistance
    # Print the value.
    print("Temperature: {0:0.3f}C".format(temp))
    print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
    # Delay for a second.
    time.sleep(1.0)






    