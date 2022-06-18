from microbit import *
import speech

while True:
    if button_a.is_pressed():
        speech.say('Current temperature is ' + str(temperature()))