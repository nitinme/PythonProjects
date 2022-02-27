#Creating a timer using python
import time
t = int(input("How many seconds do you want to countdown from? (Answer in seconds)"))

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        time_sec-=1
    print("The timer is done")    
countdown(t)


import winsound
duration = 1000 # milliseconds
freq = 440 # Hz
winsound.Beep(freq, duration)     