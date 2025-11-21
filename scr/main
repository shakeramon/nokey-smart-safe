// main 
#!/usr/bin/env python3
import sys, signal, time
import RPi.GPIO as GPIO
from lcd_utils import show
from rfid_utils import scan_tag
from keypad_utils import setup_keypad, scan_key
from assign_process import assign_process
from release_process import release_process
from servo_utils import cleanup_servos

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

setup_keypad()

def bye(*_):
    show("Shutting down","")
    cleanup_servos()
    sys.exit(0)

signal.signal(signal.SIGINT, bye)

show("Tap Card OR","Press Key")
print("System Ready (BCM Modular)")

while True:
    uid = scan_tag()
    if uid:
        assign_process(uid)
        time.sleep(1)
        continue

    key = scan_key()
    if key:
        release_process()
