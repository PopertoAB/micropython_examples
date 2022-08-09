from machine import Pin
import time

ledRed = Pin(15, Pin.OUT)
ledGreen = Pin(2, Pin.OUT)
ledBlue = Pin(4, Pin.OUT)
ledYellow = Pin(5, Pin.OUT)

def toggle(pin):
    if pin.value():
        pin.off()
    else:
        pin.on()

def task1():
    toggle(ledBlue)
    
def task2():
    toggle(ledGreen)

ledRed.off()
ledGreen.off()
ledBlue.on()
ledYellow.off()

while True:
    # Run the first task
    task1()
    
    # Run the second task
    task2()
    
    # Delay 150 ms
    time.sleep_ms(150)