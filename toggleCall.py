import RPi.GPIO as GPIO
import subprocess, os

GPIO.setmode(GPIO.BCM)

TOGGLE_PIN = 17   # Change this PIN number to your button PIN

GPIO.setup(TOGGLE_PIN, GPIO.IN)

value = 0
led_last = False
while(True):
    input = GPIO.input(TOGGLE_PIN)
 	
    if(input == 1 and value != input):
        print("Calling")
        value = input
        led_last = not led_last
        start = subprocess.run(['sudo', './RPi_Cam_Web_Interface/start.sh'])
        talk = subprocess.run(['sudo', './home/talkkonnect/bin/talkkonnect'])
    elif(input == 0 and value != input):
        print("Ending Call")
        subprocess.run(['sudo', './RPi_Cam_Web_Interface/stop.sh'])
        os.system('sudo pkill talkkonnect')
        value = 0