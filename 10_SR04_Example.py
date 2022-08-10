# Import libraries (don't forget to add hcsr04.py)
# https://github.com/rsc1975/micropython-hcsr04
from hcsr04 import HCSR04
from machine import Pin
import time

# Define trigger and echo pins
trigger = 5
echo = 18

# Create sensor
sensor = HCSR04(trigger, echo)

# Infinite loop
while True:
    print(sensor.distance_mm(), " mm")
    time.sleep(1)