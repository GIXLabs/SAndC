import board
import digitalio
import time
from LLS import LLS
from adafruit_hx711.analog_in import AnalogIn
from adafruit_hx711.hx711 import HX711

# Initialize Pins
data = digitalio.DigitalInOut(board.D5)
data.direction = digitalio.Direction.INPUT
clock = digitalio.DigitalInOut(board.D6)
clock.direction = digitalio.Direction.OUTPUT


# Constructor for HX711 Object, available gains: 128 or 64
hx = HX711(data, clock)
channel_a = AnalogIn(hx, HX711.CHAN_A_GAIN_128)

# Set Offset (Zeroing Out)
offset = sum([channel_a.value for i in range(20)]) / 20
hx.tare_value_a = offset

# Dictionary to hold data readings
dataDict = {}		


# Number of Data Points to Collect
while True:
    
    try:
        numPoints = int(input("\nPlease Enter the Number of Data Points for Linear Regression\n\n"))
        
    except ValueError:
        print("\nPlease enter an integer\n")
        continue
    
    else:
        break
    

# Collect Data Points
while True:
    
    try:
        weight = float(input("\nPlease Enter the Number of Gram(s) of the Weight (Enter -1 to Exit)\n\n"))
        
    except ValueError:
        print("\nPlease input a number\n")
        continue
    
    
    if weight == -1:
        break
    
    input("\nPlease put specified weight on the scale (Press Enter to continue)\n\n")
    
    print("\nCollecting Data Please Wait...\n")
    
    
    
    weight = int(weight)
    
    if weight not in dataDict.keys():
        dataDict[weight] = [channel_a.value]
        time.sleep(.02)
        
    for _ in range(numPoints - 1):
        dataDict[weight].append(channel_a.value)
        time.sleep(.01)
        
        
    ans = input("\nPlease remove weight from scale (Press Enter to continue or -1 to Exit)\n\n")
    
    if ans == '-1':
        break
    
    print("Sleeping for five seconds to allow strain gauge to stabilize\n\n")
    time.sleep(5)



# Convert Dictionary to two lists to perform Linear Regression

x = []
y = []

for keys, values in dataDict.items():
    y.extend([keys] * len(values))
    x.extend(values)
    
# Perform Linear Regression
m, b = LLS(x, y)

print(f"Calculated Slope from Linear Regression: {m}\n\n")
print(f"Calculated Intercept from Linear Regression: {b}\n\n")

input("Press Enter begin taking readings in Grams using values from Linear Regression (Press CTRL + C to Stop)\n\n")

while True:
    
    temp = channel_a.value
    grams = m * temp + b
    print(f"{grams} g\n")
    