import micropython
from machine import Pin
import time
import _thread

micropython.alloc_emergency_exception_buf(100)

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
    while True:
        toggle(ledBlue)
        time.sleep_ms(150)
    
def task2():
    while True:
        toggle(ledGreen)
        time.sleep_ms(150)

ledRed.off()
ledGreen.off()
ledBlue.on()
ledYellow.off()

_thread.start_new_thread(task1, ())
_thread.start_new_thread(task2, ())

TimeStart = time.ticks_ms()

while True:
    time.sleep_ms(5000)
    SecondsLive = time.ticks_diff(time.ticks_ms(), TimeStart) / 1000
    print("Executing for ", SecondsLive, " seconds")