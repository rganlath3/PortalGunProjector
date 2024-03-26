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
    #setAllBlueStatic()
    setAllBlueAnim1()


def callback_OrangeButton_Pressed():
    print("Shooting Orange Portal!")
    playRandomAudioFile("R")
    #setAllOrangeStatic()
    setAllOrangeAnim1()

def setAllOrangeStatic():
    FWD_Pixel[0] = (255, 30, 0) #Orange
    for x in range(0,28):
        AFT_Pixel[x]=(255,30,0)
        

def setAllBlueStatic():
    FWD_Pixel[0] = (0, 0, 255) #Blue
    for x in range(0,28):
        AFT_Pixel[x]=(0,0,255)



# Define colors for neopixels
Color_Red_Bright = (255, 0, 0)
Color_Orange_Dim = (25, 3, 0)
Color_Orange_Bright = (255, 30, 0)
Color_Blue_Bright = (0, 25, 255)
Color_Blue_Dim = (0, 0, 25)
Color_Teal_Bright = (25,25,255)




def setAllBlueAnim1():
    FWD_Pixel[0] = (0, 0, 255) #Blue

    for i in range(0,30):
        AFT_Pixel.fill(Color_Blue_Dim)
        if i < 28 - 2:
            AFT_Pixel[i] = Color_Blue_Bright
            AFT_Pixel[i + 2] = Color_Blue_Bright
            AFT_Pixel[i + 1] = Color_Teal_Bright
        else:
            AFT_Pixel[30 - 2] = Color_Blue_Bright
            AFT_Pixel[30 - 1] = Color_Blue_Bright
        AFT_Pixel.show()
        time.sleep(0.0005)

def setAllOrangeAnim1():
    FWD_Pixel[0] = (255, 30, 0) #Orange
    for i in range(0,30):
        AFT_Pixel.fill(Color_Orange_Dim)
        if i < 28 - 2:
            AFT_Pixel[i] = Color_Red_Bright
            AFT_Pixel[i + 2] = Color_Red_Bright
            AFT_Pixel[i + 1] = Color_Orange_Bright
        else:
            AFT_Pixel[30 - 2] = Color_Red_Bright
            AFT_Pixel[30 - 1] = Color_Red_Bright
        AFT_Pixel.show()
        time.sleep(0.0005)
        

pygame.init()

BlueButton = Button(17,bounce_time=0.1) #Blue Pushbutton
OrangeButton = Button(15,bounce_time=0.1) #Orange Pushbutton

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1)
AFT_Pixel = neopixel.NeoPixel(board.D18, 31, brightness=1) #There is actually only 29, but for animations, I am adding an extra 2 LEDs.



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
























