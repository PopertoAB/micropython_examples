# Import libraries
from machine import Pin

# Define pins
led = Pin(2, Pin.OUT)
switch = Pin(5, Pin.IN, Pin.PULL_UP)

# Infinite loop
while True:
    digitalVal = switch.value()
    if digitalVal == 1:
        led.off()
    else:
        led.on()