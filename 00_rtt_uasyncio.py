import uasyncio as asyncio
from machine import Pin

ledRed = Pin(15, Pin.OUT)
ledGreen = Pin(2, Pin.OUT)
ledBlue = Pin(4, Pin.OUT)
ledYellow = Pin(5, Pin.OUT)

def toggle(pin):
    if pin.value():
        pin.off()
    else:
        pin.on()

async def task1():
    while True:
        toggle(ledBlue)
        await asyncio.sleep_ms(150)
    
async def task2():
    while True:
        toggle(ledGreen)
        await asyncio.sleep_ms(150)
        
ledRed.off()
ledGreen.off()
ledBlue.on()
ledYellow.off()

loop = asyncio.get_event_loop()
loop.create_task(task1())
loop.create_task(task2())
loop.run_forever()