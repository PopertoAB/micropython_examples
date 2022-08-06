from machine import Pin, PWM
import time

pwm2 = PWM(Pin(2, Pin.PULL_UP), duty = 1023)
pwm4 = PWM(Pin(4, Pin.PULL_UP), duty = 0)
pwm5 = PWM(Pin(5, Pin.PULL_UP), duty = 0)
print(pwm2)
print(pwm4)
print(pwm5)

delay_time = 10

while True:

    redValue = 255
    greenValue = 0
    blueValue = 0

    for i in range(0, 256):
        redValue = 255 - i
        greenValue = i
        
        pwm2.duty(redValue * 4)
        pwm4.duty(greenValue * 4)
        time.sleep_ms(delay_time)

    redValue = 0
    greenValue = 255
    blueValue = 0

    for i in range(0, 256):
        greenValue = 255 - i
        blueValue = i
        
        pwm4.duty(greenValue * 4)
        pwm5.duty(blueValue * 4)
        time.sleep_ms(delay_time)

    redValue = 0
    greenValue = 0
    blueValue = 255

    for i in range(0, 256):
        blueValue = 255 - i
        redValue = i
        
        pwm5.duty(blueValue * 4)
        pwm2.duty(redValue * 4)
        time.sleep_ms(delay_time)
