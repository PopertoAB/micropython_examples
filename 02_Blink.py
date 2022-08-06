# Import libraries
from machine import Pin
import time

# Define a function to toggle the pin
def toggle(pin):
    if pin.value():
        pin.value(0)
    else:
        pin.value(1)

# Define built-in pin
p2 = Pin(2, Pin.OUT, Pin.PULL_UP)

while True:
    toggle(p2)
    time.sleep(1)