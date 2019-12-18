from adafruit_motor import servo
from analogio import AnalogIn
import pulseio
import board
import digitalio
from time import sleep

pwm = pulseio.PWMOut(board.D7, frequency=50)

contserv = servo.ContinuousServo(pwm)

pot = AnalogIn(board.A0)

photo = digitalio.DigitalInOut(board.D2)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP

photo2 = digitalio.DigitalInOut(board.D3)
photo2.direction = digitalio.Direction.INPUT
photo2.pull = digitalio.Pull.UP

photo_state = False
last_state = False

photo2_state = False
last2_state = False

led = digitalio.DigitalInOut(board.D8)
led2 = digitalio.DigitalInOut(board.D9)
led3 = digitalio.DigitalInOut(board.D10)
led4 = digitalio.DigitalInOut(board.D11)

led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT

value = 0

while True:
    print(pot.value)

    sleep(1)

    if pot.value <= 32000:
        contserv.throttle = 1.0
    if pot.value > 32000:
        contserv.throttle = -1.0

    '''
    if pot.value <= 800:
        contserv.throttle = 0
    if pot.value > 800 & pot.value <= 6800:
        contserv.throttle = 0.1
    if pot.value > 6800 & pot.value <= 12800:
        contserv.throttle = 0.2
    if pot.value > 12800 & pot.value <= 18800:
        contserv.throttle = 0.3
    if pot.value > 18800 & pot.value <= 24800:
        contserv.throttle = 0.4
    if pot.value > 24800 & pot.value <= 30800:
        contserv.throttle = 0.5
    if pot.value > 30800 & pot.value <= 36800:
        contserv.throttle = 0.6
    if pot.value > 36800 & pot.value <= 46800:
        contserv.throttle = 0.7
    if pot.value > 46800 & pot.value <= 52800:
        contserv.throttle = 0.8
    if pot.value > 52800 & pot.value <= 60800:
        contserv.throttle = 0.9
    if pot.value > 60800 & pot.value <= 66800:
        contserv.throttle = 1.0
    '''
    photo_state = photo.value
    photo2_state = photo2.value

    if photo_state and not last_state:
        value += 1
    last_state = photo_state

    if photo2_state and not last2_state:
        value = value + 1
    last2_state = photo2_state

    print(value)

    led.value = True
    led2.value = True
    led3.value = True
    led4.value = True

    if value == 1:
        led.value = False
        led2.value = False
        led3.value = False
        led4.value = True
    if value == 2:
        led.value = False
        led2.value = False
        led3.value = True
        led4.value = False
    if value == 3:
        led.value = False
        led2.value = False
        led3.value = True
        led4.value = True
    if value == 4:
        led.value = False
        led2.value = True
        led3.value = False
        led4.value = False
    if value == 5:
        led.value = False
        led2.value = True
        led3.value = False
        led4.value = True
    if value == 6:
        led.value = False
        led2.value = True
        led3.value = True
        led4.value = False
    if value == 7:
        led.value = False
        led2.value = True
        led3.value = True
        led4.value = True
    if value == 8:
        led.value = True
        led2.value = False
        led3.value = False
        led4.value = False
    if value == 9:
        led.value = True
        led2.value = False
        led3.value = False
        led4.value = True
    if value == 10:
        led.value = True
        led3.value = False
        led2.value = True
        led4.value = False
    if value == 11:
        led.value = True
        led2.value = False
        led3.value = True
        led4.value = True
    if value == 12:
        led.value = True
        led2.value = True
        led3.value = False
        led4.value = False
    if value == 13:
        led.value = True
        led2.value = True
        led3.value = False
        led4.value = True
    if value == 14:
        led.value = True
        led2.value = True
        led3.value = True
        led4.value = False
    if value == 15:
        led.value = True
        led2.value = True
        led3.value = True
        led4.value = True
