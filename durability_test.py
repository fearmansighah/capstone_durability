import os
import time


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



while True:
    measurements = f'{timenow}, {measure_temp()}, {measure_core()}, {measure_arm()}'
    print(measurements, '\n')

    with open('readings.txt', "a") as file:
        file.write(measurements + "\n")

    time.sleep(1)
    timenow += 1
