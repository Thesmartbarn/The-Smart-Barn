import RPi.GPIO as IO

FAN_ON = 13
FAN_OFF = 19

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(FAN_ON, IO.OUT)
IO.setup(FAN_OFF, IO.OUT)


def setFanStatus(calculatedSpeed):
    if calculatedSpeed == 0: 
        IO.output(FAN_OFF, IO.LOW)
        IO.output(FAN_ON, IO.HIGH)
    else:
        IO.output(FAN_ON, IO.LOW)
        IO.output(FAN_OFF, IO.HIGH)

