from LEDControl import LEDControl
from machine import Pin, ADC, PWM
import _thread
import utime

led = LEDControl()
leds = list()

# Assign PWMs
pins = [16, 17, 18]
for i in pins:
    leds.append(PWM(Pin(i)))
for i in range(len(leds)):
    leds[i].freq(1000)

# Loop that sets function for LEDs
while True:
    
    # Function from LED class
    led.fadeup()
    
    # Write values to LED PWMs
    for i in range(len(leds)):
        leds[i].duty_u16(led.pwmconvert(led.led[i]))
