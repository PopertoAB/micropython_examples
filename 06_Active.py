# Import libraries
from machine import Pin
import time

# Define buzzer pin
buzzer = Pin(5, Pin.OUT)

# Infinite loop
while True:
    for i in range(0, 80):
        buzzer.on()
        time.sleep_ms(1)
        buzzer.off()
        time.sleep_ms(1)
        
    for i in range(0, 99):
        buzzer.on()
        time.sleep_ms(2)
        buzzer.off()
        time.sleep_ms(2)