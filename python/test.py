import pigpio
import requests
from time import sleep

PIN = 16

pi = pigpio.pi()
pi.set_mode(PIN, pigpio.INPUT)
pi.set_pull_up_down(PIN, pigpio.PUD_DOWN)

prev = 0

while True:
    now = pi.read(PIN)
    if now == 0 and prev == 1 :
        print "rotate!"
        requests.get("http://esp8266.local/rotate")
    elif now == 1 and prev == 0:
        print "reverse!"
        requests.get("http://esp8266.local/reverse")

    prev = now
    sleep(0.1)
