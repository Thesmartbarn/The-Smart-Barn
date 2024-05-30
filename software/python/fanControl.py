import RPi.GPIO as IO
import board
import digitalio
import adafruit_max31865
import adafruit_dht


FAN_ON = 13
FAN_OFF = 19

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(FAN_ON, IO.OUT)
IO.setup(FAN_OFF, IO.OUT)

IO.setmode(IO.BCM)
IO.setup(18, IO.OUT)
pwm = IO.PWM(18, 50)
pwm.start(0)

# temp sensor
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
tempSensor = adafruit_max31865.MAX31865(spi, cs)

#hum sensor
dht11 = adafruit_dht.DHT11(board.D17)

def setFanSpeed(fanSpeed):
    if fanSpeed == 0: 
        IO.output(FAN_OFF, IO.LOW)
        IO.output(FAN_ON, IO.HIGH)
    else:
        IO.output(FAN_ON, IO.LOW)
        IO.output(FAN_OFF, IO.HIGH)
        pwm.ChangeDutyCycle(fanSpeed)

def readTempSensor():
    temp = tempSensor.temperature
    return temp if temp != None else 0

def readHumSensor():
    
    hum = dht11.humidity
    return hum if hum != None else 0



