# Define libraries
from machine import Pin
import time

# Define pins
led = Pin(2, Pin.OUT)
button_on = Pin(4, Pin.IN, Pin.PULL_UP)
button_off = Pin(5, Pin.IN, Pin.PULL_UP)

# Main loop
while True:
    if button_on.value() == 0:
        led.on()
    el if button_off.value() == 0:
        led.off()