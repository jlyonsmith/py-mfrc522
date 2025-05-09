#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(22, 0)
GPIO.output(20, 1)

reader = SimpleMFRC522()

try:
        version = reader.read_version()
        print(version)
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
