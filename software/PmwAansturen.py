
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(0)

while True:
    PwmWaarde = int(input("geef een pmw waarde in: "))
    pwm.ChangeDutyCycle(PwmWaarde)