import RPi.GPIO as GPIO
import subprocess, os, time

GPIO.setmode(GPIO.BCM)

TOGGLE_PIN = 17   # Change this PIN number to your button PIN

GPIO.setup(TOGGLE_PIN, GPIO.IN)

on = False
while(True):
    input = GPIO.input(TOGGLE_PIN)
    if input == 0:
        #if on == False:
        print("Calling")
        os.system('sudo sh /home/tradeview01/RPi_Cam_Web_Interface/start.sh')
        subprocess.run(['sudo', '/home/talkkonnect/bin/talkkonnect'])
        print("Ending Call")
        os.system('sudo sh /home/tradeview01/RPi_Cam_Web_Interface/stop.sh')
        input = 1
        time.sleep(5)
        #on = True
        '''elif on == True:
            print("Ending Call")
            subprocess.run(['sudo', './RPi_Cam_Web_Interface/stop.sh'])
            os.system('sudo pkill talkkonnect')
            input = 1
            time.sleep(5)
            on = False'''
'''
    if(input == 1 and value != input):
        print("Calling")
        value = input
        start = subprocess.run(['sudo', './RPi_Cam_Web_Interface/start.sh'])
        #talk = subprocess.run(['sudo', '/home/talkkonnect/bin/talkkonnect'])
    elif(input == 0 and value != input):
        print("Ending Call")
        subprocess.run(['sudo', './RPi_Cam_Web_Interface/stop.sh'])
        #os.system('sudo pkill talkkonnect')
        value = 0'''