# Import libraries
from machine import Pin, PWM
import time

# Pitches
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988
NOTE_C6 = 1047

# Time between notes
duration = 500

# Setup pins
buzzer = PWM(Pin(5))
melody = (NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6)

# Infinite loop
while True:
    for i in melody:
        buzzer.freq(i)
        time.sleep_ms(duration)
