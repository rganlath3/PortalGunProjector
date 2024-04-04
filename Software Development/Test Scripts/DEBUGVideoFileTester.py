#If running as sudo (required for neopixels), VLC complains. The key is to run this command:
# sudo sed -i 's/geteuid/getppid/' /usr/bin/vlc

#This attempt uses VLC CLI to run videos.
from gpiozero import Button
from signal import pause
import subprocess
import random
import pygame

# VIDEO SETUP
VideoPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/"
VBP_count = 4 #Store number of BP_.wav files in Audio Directory
VOP_count = 4 #Store number of OP_.wav files in Audio Directory
current_process = None # Global variable to store the currently playing process

def playVideo(video_path):
    global current_process
    # Stop the currently playing video, if any
    if current_process:
        current_process.kill()
    # Play the new video
    cmd = ["vlc", video_path,"--loop", "--no-video-title", "--fullscreen", "--no-qt-fs-controller"]
    current_process = subprocess.Popen(cmd)



def playRandomVideoFile(msg):
    #Takes in a str and based on that randomly plays a video in the sounds directory that starts with str.
    #Types of commands:
    #OP is for orange portals
    #BP is for blue portals

    global VideoPath,VBP_count,VOP_count
    cmd = VideoPath + msg 
    if(msg == 'BP'):
        cmd = cmd + str(random.randint(1,VBP_count)) #adjust randint values based on number of sounds in directory.
    if(msg == 'OP'):
        cmd = cmd + str(random.randint(1,VOP_count))
    cmd = cmd + ".mp4"
    playVideo(cmd)


def callback_BlueButton_Pressed():
    #playVideoBlue()
    playRandomVideoFile("BP")

def callback_OrangeButton_Pressed():
    #playVideoOrange()
    playRandomVideoFile("OP")

#Initialize buttons
BlueButton = Button(17,bounce_time=0.1)
OrangeButton = Button(15,bounce_time=0.1)


# Initializing Pygame
pygame.init()
 
# Initializing surface
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN)

# Initializing RGB Color
color = (0, 0, 0)
    
# Changing surface color
surface.fill(color)
pygame.display.update()


# Assign button callbacks
BlueButton.when_released = callback_BlueButton_Pressed
OrangeButton.when_released = callback_OrangeButton_Pressed

print("Setup Complete, Ready for Portals")
pause()
