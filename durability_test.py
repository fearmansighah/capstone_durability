import os
import time
#import board
#import adafruit_am2320


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp.replace("temp=", "")
    temp.replace("'C", "")
    return (temp.replace("temp=", ""))


def measure_freq():
    freq = os.popen('vcgencmd measure_clock arm').readline()
    freq = freq.replace("frequency(48)=", "")
    freq = int(freq)/10000
    return (freq)


# create venv
# python3 -m venv venv
# source .venv/bin/activate
# (sudo) pip3 install adafruit-circuitpython-am2320


# create the I2C shared bus
# i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
#am = adafruit_am2320.AM2320(i2c)
timenow = 0

while True:
    # timestamp, core temp, # arm freq, # sensor temp, # sensor hum
    #print(timestamp(), measure_temp(), measure_freq(), am.temperature, am.relative_humdiity)
    #print(timestamp(), measure_temp(), measure_freq())

    measurements = f'{timenow}, {measure_temp()}, {measure_freq()}'

    with open('readings.txt', "a") as file:
        file.write(measurements + "\n")

    time.sleep(1)
    timenow += 1
