from digitalio import DigitalInOut, Direction, Pull
import board
import time

interpt_pin = DigitalInOut(board.D6)
interpt_pin.direction = Direction.INPUT
interpt_pin.pull = Pull.UP

interrupts = 0

interpt_state = False
last_state = False

max = 4
start = time.monotonic()
while True:
    interpt_state = interpt_pin.value
    if interpt_state and not last_state:
        interrupts += 1
    last_state = interpt_state

    # This will be updated every loop
    remaining = max + start - time.monotonic()
    # When countdown ends, prints value
    if remaining <= 0:
        print("Interrupts:", str(interrupts))
        max += 4
        interrupts = 0