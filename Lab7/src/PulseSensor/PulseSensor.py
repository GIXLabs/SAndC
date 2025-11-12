import time
import board
import digitalio
from analogio import AnalogIn

ppg = AnalogIn(board.A0)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

threshold = 45000


while True:
    
    print(ppg.value)
    
    if ppg.value > threshold:
        led.value = False
    else:
        led.value = True
        
    time.sleep(.05)
    
