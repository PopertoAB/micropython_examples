from machine import Pin, Timer
import time
import micropython

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

def task1(timer):
    toggle(ledBlue)
    return
    
def task2(timer):
    toggle(ledGreen)
    return

ledRed.off()
ledGreen.off()
ledBlue.on()
ledYellow.off()

# Create task timer for Blue LED
tim0 = Timer(0)
tim0.init(period=200, mode=Timer.PERIODIC, callback=task1)
print("Task 1 - Blue LED toggle initialized ...")

# Create task timer for Green LED
tim1 = Timer(1)
tim1.init(period=200, mode=Timer.PERIODIC, callback=task2)
print("Task 2 - Green LED toggle initialized ...")

TimeStart = time.ticks_ms()

while True:
    time.sleep_ms(5000)
    SecondsLive = time.ticks_diff(time.ticks_ms(), TimeStart) / 1000
    print("Executing for ", SecondsLive, " seconds")