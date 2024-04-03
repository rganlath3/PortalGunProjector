#!/usr/bin/env python3

#5 PushButton with Neopixel with Randomized Sounds
#Made by Ranil Ganlath 03-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#PushButton Support
#NeoPixel Static Test
#Randomized Sounds
#Bootup Sounds

import time
import board
import neopixel
from gpiozero import Button
from signal import pause
import pygame
import random
import subprocess

# AUDIO PART
global AudioPath #Stores Audio Directory Folder Path
global R_count #Store number of R_.wav files in Audio Directory
global B_count #Store number of B_.wav files in Audio Directory
global P_count #Store number of P_.wav files in Audio Directory

#Find Audio Directory
AudioPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Sounds/"

#DEVELOPER note I should hardcode these values in to save on startup time.
#Now we count how many of each type of file is in this audio directory to dynamically adjust to new sound files added.
# Get the list of files in the directory that contain a letter like 'R'
result = subprocess.run(['ls', AudioPath], stdout=subprocess.PIPE, universal_newlines=True)
R_count = len([filename for filename in result.stdout.split() if 'R' in filename])
B_count = len([filename for filename in result.stdout.split() if 'B' in filename])
P_count = len([filename for filename in result.stdout.split() if 'P' in filename])
print("Number of files with 'R' in the filename: ", R_count)
print("Number of files with 'B' in the filename: ", B_count)
print("Number of files with 'P' in the filename: ", P_count)



def playRandomAudioFile(msg):
    #Takes in a str and based on that randomly plays a song in the sounds directory that starts with str.
    #Types of commands:
    #R is for red portals
    #B is for blue portals
    #P is for misc sounds

    global AudioPath
    global R_count
    global B_count
    global P_count
    cmd = AudioPath + msg 
    if(msg=='R'):
        cmd = cmd + str(random.randint(1,R_count)) #adjust randint values based on number of sounds in directory. Hardcoded for now since i have better things to do.
    if(msg =='B'):
        cmd = cmd + str(random.randint(1,B_count))
    if(msg == 'P'):
        cmd = cmd + str(random.randint(1,P_count))
    
    cmd = cmd + ".wav" #append .wav to the end
    sound = pygame.mixer.Sound(cmd)
    sound.play()




def callback_BlueButton_Pressed():
    print("Shooting Blue Portal!")
    playRandomAudioFile("B")
    setAllBlueStatic()

def callback_OrangeButton_Pressed():
    print("Shooting Orange Portal!")
    playRandomAudioFile("R")
    setAllOrangeStatic()

def setAllOrangeStatic():
    FWD_Pixel[0] = (255, 30, 0) #Orange
    for x in range(0,28):
        AFT_Pixel[x]=(255,30,0)
        

def setAllBlueStatic():
    FWD_Pixel[0] = (0, 0, 255) #Blue
    for x in range(0,28):
        AFT_Pixel[x]=(0,0,255)

       

pygame.init()

BlueButton = Button(17,bounce_time=0.1) #Blue Pushbutton
OrangeButton = Button(15,bounce_time=0.1) #Orange Pushbutton

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1)
AFT_Pixel = neopixel.NeoPixel(board.D18, 29, brightness=1)



#Setup Function (Runs once on powerup)

playRandomAudioFile("P") #Startup Sound
print("Setup Complete")

#Loop Function
while True:
    #Wait for a button to be pressed
    #Using Released due to pullup resistor
    BlueButton.when_released = callback_BlueButton_Pressed
    OrangeButton.when_released = callback_OrangeButton_Pressed
    pause()
























