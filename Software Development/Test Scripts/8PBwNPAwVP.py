#!/usr/bin/env python3

#8 PushButton with Neopixel Animations with Video Playback
#Made by Ranil Ganlath 04-02-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#PushButton Support
#NeoPixel Animations
#Randomized Sounds and Video Playback
#Bootup Animations and Sounds and Video Playback
#File Paths are now relative.

#TO DO
""" 
Add 2nd channel for playing ambience music. This may or may not get paused when a portal blast is played. 
Test if ambience repeats nicely without pause.
Instead of using .desktop for startup, find alternate since it doesn't work with the CLI tool.
 """

import time
import board
import neopixel
from gpiozero import Button
from signal import pause
import pygame
import random
import math
import vlc
import pathlib

#NEOPIXEL SETUP
NUM_PIXELS = 31
Color_Red_Bright = (255, 0, 0)
Color_Orange_Dim = (25, 3, 0)
Color_Orange_Bright = (255, 30, 0)
Color_Blue_Bright = (0, 25, 255)
Color_Blue_Dim = (0, 0, 25)
Color_Teal_Bright = (25,25,255)
Color_Black = (0,0,0)
Color_White = (255, 255, 255)


def getPath(pathType):
    if pathType=="video":
        path = path = str(pathlib.Path(__file__)) #get the file path where this script is stored.
        index = path.rfind("PortalGunProjector")
        if index != -1:
            path = path[:index + len("PortalGunProjector")] + "/Software Development/Videos/"
            return path
        else:
            print("Can't find that path")
    if pathType=="audio":
        path = path = str(pathlib.Path(__file__)) #get the file path where this script is stored.
        index = path.rfind("PortalGunProjector")
        if index != -1:
            path = path[:index + len("PortalGunProjector")] + "/Software Development/Sounds/"
            return path
        else:
            print("Can't find that path")
    print("Error not valid path type")
    return "ERROR"





# AUDIO SETUP
AudioPath = getPath("audio")
R_count = 6 #Store number of R_.wav files in Audio Directory
B_count = 6 #Store number of B_.wav files in Audio Directory
P_count = 7 #Store number of P_.wav files in Audio Directory
A_count = 2 #Store number of R_.wav files in Audio Directory
M_count = 5 #Store number of B_.wav files in Audio Directory
T_count = 5 #Store number of P_.wav files in Audio Directory

# VIDEO SETUP
VideoPath = getPath("video")
VBP_count = 4 #Store number of BP_.mp4 files in Audio Directory
VOP_count = 4 #Store number of OP_.mp4 files in Audio Directory
VBoot_count = 5 #Store number of Boot.mp4 files in Audio Directory

###############################################################
#######################FUNCTIONS DEFINITIONS###################
###############################################################     


def playRandomAudioFile(msg):
    #Takes in a str and based on that randomly plays a song in the sounds directory that starts with str.
    #Types of commands:
    #A is for ambience, play this on a side channel
    #R is for red portals
    #B is for blue portals
    #P is for bootup sounds, play this as a fun quote during bootup.

    global AudioPath,R_count,B_count,P_count
    cmd = AudioPath + msg 
    if(msg == 'R'):
        cmd = cmd + str(random.randint(1,R_count)) #adjust randint values based on number of sounds in directory.
    if(msg == 'B'):
        cmd = cmd + str(random.randint(1,B_count))
    if(msg == 'P'):
        cmd = cmd + str(random.randint(1,P_count))
    if(msg == 'A'):
        cmd = cmd + str(random.randint(1,A_count))
    if(msg == 'M'):
        cmd = cmd + str(random.randint(1,M_count))
    if(msg == 'T'):
        cmd = cmd + str(random.randint(1,T_count))
    cmd = cmd + ".wav"
    SoundFile = pygame.mixer.Sound(cmd)
    SoundFile.play()
    return SoundFile.get_length()

def playVideo(desiredIndex):
    media_player.play_item_at_index(desiredIndex) 

    
def playRandomVideoFile(msg):
    #Takes in a str and based on that randomly plays a video in the sounds directory that starts with str.
    #Types of commands:
    #OP is for orange portals
    #BP is for blue portals

    global VideoPath,VBP_count,VOP_count
    cmd = VideoPath + msg 
    if(msg == 'BP'):
        playVideo(random.randint(0,3))
    if(msg == 'OP'):
        playVideo(random.randint(4,7)) 
        #fix this to not be hardcoded, ex. starting range could be VBP_count to VBP_count + VOP_count
    if(msg == 'BOOT'):
        playVideo(random.randint(8,12)) 
        #fix this to not be hardcoded, ex. starting range could be VBP_count to VBP_count + VOP_count

def callback_BlueButton_Pressed():
    #Runs when blue button is pressed
    #print("Shooting Blue Portal!")
    playRandomVideoFile("BP")
    playRandomAudioFile("B")
    playRandomBlueAnimation()


def callback_OrangeButton_Pressed():
    #Runs when orange button is pressed
    #print("Shooting Orange Portal!")
    playRandomVideoFile("OP")
    playRandomAudioFile("R")
    playRandomOrangeAnimation()



def playRandomOrangeAnimation():
    global Color_Orange_Bright, Color_Orange_Dim, Color_Red_Bright
    Color_Orange_Bright = modify_color(Color_Orange_Bright)
    #Color_Orange_Dim = modify_color(Color_Orange_Dim)
    Color_Red_Bright = modify_color(Color_Red_Bright)

    FWD_Pixel[0] = (255, 30, 0) #Orange
    roll = random.randint(0,2)
    if roll == 0:
        print("Shooting Orange Portal 1!")
        OrangePortalAnim1()
    if roll == 1:
        print("Shooting Orange Portal 2!")
        OrangePortalAnim2()
    if roll == 2:
        print("Shooting Orange Portal 3!")
        OrangePortalAnim3()


def playRandomBlueAnimation():
    global Color_Blue_Bright, Color_Blue_Dim, Color_Teal_Bright
    Color_Blue_Bright =modify_color(Color_Blue_Bright)
    #Color_Blue_Dim =modify_color(Color_Blue_Dim)
    Color_Teal_Bright =modify_color(Color_Teal_Bright)

    FWD_Pixel[0] = (0, 0, 255) #Blue
    roll = random.randint(0,2)
    if roll == 0:
        print("Shooting Blue Portal 1!")
        BluePortalAnim1()
    if roll == 1:
        print("Shooting Blue Portal 2!")
        BluePortalAnim2()

    if roll == 2:
        print("Shooting Blue Portal 3!")
        BluePortalAnim3()




###############################################################
#######################LED ANIMATIONS##########################
###############################################################   
        

def setAllOrangeStatic():
    #Sets all LEDs Orange
    FWD_Pixel[0] = (255, 30, 0) #Orange
    for x in range(0,28):
        AFT_Pixel[x]=(255,30,0)
        
def setAllBlueStatic():
    #Sets all LEDs Blue
    FWD_Pixel[0] = (0, 0, 255) #Blue
    for x in range(0,28):
        AFT_Pixel[x]=(0,0,255)

def BluePortalAnim1():
    for i in range(0,NUM_PIXELS):
        AFT_Pixel.fill(Color_Blue_Dim)
        if i < NUM_PIXELS - 2:
            AFT_Pixel[i] = Color_Blue_Bright
            AFT_Pixel[i + 2] = Color_Blue_Bright
            AFT_Pixel[i + 1] = Color_Teal_Bright
        else:
            AFT_Pixel[NUM_PIXELS - 2] = Color_Blue_Bright
            AFT_Pixel[NUM_PIXELS - 1] = Color_Blue_Bright
        AFT_Pixel.show()
        time.sleep(0.0005)

def BluePortalAnim2():
    timedelay = round(random.uniform(0.005,0.002),4)
    cycle = -1 * math.pi / NUM_PIXELS  # Wave cycle based on the number of pixels
    for t in range(10):
        AFT_Pixel.fill(Color_Blue_Dim)  # Clear pixels
        for i in range(NUM_PIXELS):
            brightness = (math.cos(i * cycle + t * 0.2) + 1) / 2  # Calculate brightness based on sine wave
            AFT_Pixel[i] = tuple(int(brightness/3 * c) for c in Color_Teal_Bright)  # Apply adjusted color to pixel
        AFT_Pixel.show()
        time.sleep(timedelay)
    for x in range(0,NUM_PIXELS):
        AFT_Pixel[x]=(Color_Blue_Dim)

def OrangePortalAnim1():
    timedelay = round(random.uniform(0.0002,0.002),4)
    
    for i in range(0,NUM_PIXELS):
        AFT_Pixel.fill(Color_Orange_Dim)
        if i < NUM_PIXELS - 2:
            AFT_Pixel[i] = Color_Red_Bright
            AFT_Pixel[i + 2] = Color_Red_Bright
            AFT_Pixel[i + 1] = Color_Orange_Bright
        else:
            AFT_Pixel[NUM_PIXELS - 2] = Color_Red_Bright
            AFT_Pixel[NUM_PIXELS - 1] = Color_Red_Bright
        AFT_Pixel.show()
        time.sleep(timedelay)

def OrangePortalAnim2():
    timedelay = round(random.uniform(0.005,0.002),4)
    cycle = -1 * math.pi / NUM_PIXELS  # Wave cycle based on the number of pixels
    for t in range(10):
        AFT_Pixel.fill(Color_Orange_Dim)  # Clear pixels
        for i in range(NUM_PIXELS):
            brightness = (math.cos(i * cycle + t * 0.2) + 1) / 2  # Calculate brightness based on sine wave
            AFT_Pixel[i] = tuple(int(brightness/3 * c) for c in Color_Red_Bright)  # Apply adjusted color to pixel
        AFT_Pixel.show()
        time.sleep(timedelay)
    for x in range(0,NUM_PIXELS):
        AFT_Pixel[x]=(Color_Orange_Dim)

def modify_color(color, max_change=2):
    modified_color = []
    for component in color:
        change = random.randint(-max_change, max_change)
        modified_component = max(0, min(255, component + change))
        modified_color.append(modified_component)
    return tuple(modified_color)        

def OrangePortalAnim3():
    # Initial flicker
    for _ in range(8):
        for i in range(NUM_PIXELS):
            if random.random() < 0.3:
                flicker_brightness = random.randint(0, 50)
                flicker_color = tuple(int(flicker_brightness / 100 * c) for c in Color_Red_Bright)
                AFT_Pixel[i] = flicker_color
            else:
                AFT_Pixel[i] = (Color_Orange_Dim)
        AFT_Pixel.show()
        time.sleep(0.005)
    # Gradual increase in brightness
    for brightness in range(1, 5):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = tuple(int(brightness / 100 * c) for c in Color_Orange_Bright)  # Adjust brightness
        AFT_Pixel.show()
        time.sleep(0.001)
    for x in range(0,NUM_PIXELS):
        AFT_Pixel[x]=(Color_Orange_Dim)

# Define animation function
def BluePortalAnim3():
    # Initial flicker
    for _ in range(8):
        for i in range(NUM_PIXELS):
            if random.random() < 0.3:
                flicker_brightness = random.randint(0, 50)
                flicker_color = tuple(int(flicker_brightness / 100 * c) for c in Color_Teal_Bright)
                AFT_Pixel[i] = flicker_color
            else:
                AFT_Pixel[i] = (Color_Blue_Dim)
        AFT_Pixel.show()
        time.sleep(0.005)
    # Gradual increase in brightness
    for brightness in range(1, 5):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = tuple(int(brightness / 100 * c) for c in Color_Blue_Bright)  # Adjust brightness
        AFT_Pixel.show()
        time.sleep(0.001)
    for x in range(0,NUM_PIXELS):
        AFT_Pixel[x]=(Color_Blue_Dim)

def rgb_test_animation():
    tuner = 50
    brightness_range = 3
    for brightness in range(0, brightness_range):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (brightness*tuner, 0, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (brightness*tuner, 0, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(brightness_range, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (brightness*tuner, 0, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (brightness*tuner, 0, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(0, brightness_range):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, brightness*tuner, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,brightness*tuner, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(brightness_range, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, brightness*tuner, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,brightness*tuner, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(0, brightness_range):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, 0, brightness*tuner)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,0,brightness*tuner)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(brightness_range, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, 0, brightness*tuner)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,0,brightness*tuner)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation

def bootupAnimation(duration):
    FWD_Pixel.fill(Color_White)
    start_time = time.monotonic()
    while time.monotonic() - start_time < duration:
        for i in range(NUM_PIXELS):
            for j in range(i):
                AFT_Pixel[j] = Color_White  # Set pixels up to current position to glow color
            AFT_Pixel.show()
            time.sleep(0.01)  # Adjust this value to change the speed of the animation
        AFT_Pixel.fill(Color_Black)  # Clear pixels
    AFT_Pixel.fill(Color_White)  # Clear pixels


###############################################################
###########Setup Function (Runs once on powerup)###############
###############################################################     

print("Starting Bootup")
#Initialize buttons
BlueButton = Button(17,bounce_time=0.1)
OrangeButton = Button(15,bounce_time=0.1)
#Initialize LEDs
FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1) 
AFT_Pixel = neopixel.NeoPixel(board.D18, 31, brightness=1) #There is actually only 29, but for animations, I am adding an extra 2 LEDs.

#Initialize for video playback
#Path Setup
video_files = []
for file in range(1,VBP_count+1):
    video_files.append("BP"+str(file)+".mp4")
for file in range(1,VOP_count+1):
    video_files.append("OP"+str(file)+".mp4")
for file in range(1,VBoot_count+1):
    video_files.append("BOOT"+str(file)+".mp4")

#at this point, the array is fully built, now let's iterate over it after creating our media players
# creating Instance class object 
player = vlc.Instance() 
# Create a media player object
playman = vlc.MediaPlayer()
playman.set_fullscreen(True)
playman.audio_output_set('dummy') #disable audio
# creating a media list player object 
media_player = vlc.MediaListPlayer() 
media_player.set_playback_mode(2) #repeat current video
# creating a new media list object 
media_list = player.media_list_new() 
#Add all videos to playlist
for video in range(len(video_files)):
    media = player.media_new(VideoPath+video_files[video]) # creating a new media 
    media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 
media_player.set_media_player(playman)
#Initial Bootup Video


playRandomVideoFile("BOOT")


#Initialize for audio playback
pygame.init()
#Play Bootup Sound
pygame.mixer.Sound(AudioPath+"T2.wav").play()
#RGB NEOPIXEL COLOR TEST
rgb_test_animation()
#Play a random fun quote and return the length of it.
SoundLength = (playRandomAudioFile("P")) #Startup Sound
#Play Neopixel loading animation that is soundlength long.
bootupAnimation(SoundLength)
#Play Ready Sound
pygame.mixer.Sound(AudioPath+"T1.wav").play()
print("Setup Complete, Ready for Portals")


###############################################################
#####################Loop Function#############################
###############################################################


while True:
    #Wait for a button to be pressed, (using when_released since using NC button pin)
    BlueButton.when_released = callback_BlueButton_Pressed
    OrangeButton.when_released = callback_OrangeButton_Pressed
    pause()
