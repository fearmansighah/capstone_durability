import os
import time
import board
import adafruit_am2320
import paho.mqtt.client as mqtt

# to run: sudo python3 duability_test.py


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "")
    temp = temp.replace("\n", "")
    temp = temp.replace("'C", "")
    return (temp)


def measure_arm():
    freq = os.popen('vcgencmd measure_clock arm').readline()
    freq = freq.replace("frequency(48)=", "")
    freq = int(freq)
    return (freq)


def measure_core():
    freq = os.popen('vcgencmd measure_clock core').readline()
    freq = freq.replace("frequency(1)=", "")
    freq = int(freq)
    return (freq)


# create the I2C shared bus
i2c = board.I2C()  # uses board.SCL and board.SDA
am = adafruit_am2320.AM2320(i2c)
timenow = 0
mqttBroker = "mqtt.eclipseprojects.io"
mqttClient = mqtt.Client("crwn_pi")
topic = 'durability_test'

while True:
    # timestamp, core temp, # arm freq, # sensor temp, # sensor hum
    #pr(timestamp(), measure_temp(), measure_freq(), am.temperature, am.relative_humdiity)
    measurements = f'{timenow}, {measure_temp()}, {measure_core()}, {measure_arm()}, {am.temperature}, {am.relative_humidity}'

    measurements = f'{timenow}, {measure_temp()}, {measure_core()}, {measure_arm()}'
    print(measurements, '\n')

    with open('readings.txt', "a") as file:
        file.write(measurements + "\n")

    mqttClient.connect(mqttBroker)

    mqttClient.publish(topic, measurements)

    time.sleep(1)
    timenow += 1
