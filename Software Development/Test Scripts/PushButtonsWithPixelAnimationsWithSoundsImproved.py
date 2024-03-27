import time
import board
import neopixel
from gpiozero import Button
from signal import pause
import pygame
import random
import math

#NEOPIXEL SETUP
NUM_PIXELS = 31
# Define colors for neopixels
Color_Red_Bright = (255, 0, 0)
Color_Orange_Dim = (25, 3, 0)
Color_Orange_Bright = (255, 30, 0)
Color_Blue_Bright = (0, 25, 255)
Color_Blue_Dim = (0, 0, 25)
Color_Teal_Bright = (25,25,255)


# AUDIO SETUP
AudioPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Sounds/"
R_count = 4 #Store number of R_.wav files in Audio Directory
B_count = 4 #Store number of B_.wav files in Audio Directory
P_count = 2 #Store number of P_.wav files in Audio Directory



def playRandomAudioFile(msg):
    #Takes in a str and based on that randomly plays a song in the sounds directory that starts with str.
    #Types of commands:
    #R is for red portals
    #B is for blue portals
    #P is for misc sounds

    global AudioPath,R_count,B_count,P_count
    cmd = AudioPath + msg 
    if(msg=='R'):
        cmd = cmd + str(random.randint(1,R_count)) #adjust randint values based on number of sounds in directory.
    if(msg =='B'):
        cmd = cmd + str(random.randint(1,B_count))
    if(msg == 'P'):
        cmd = cmd + str(random.randint(1,P_count))
    cmd = cmd + ".wav"
    pygame.mixer.Sound(cmd).play()

def callback_BlueButton_Pressed():
    #Runs when blue button is pressed
    print("Shooting Blue Portal!")
    playRandomAudioFile("B")
    playRandomBlueAnimation()

def callback_OrangeButton_Pressed():
    #Runs when orange button is pressed
    print("Shooting Orange Portal!")
    playRandomAudioFile("R")
    playRandomOrangeAnimation()


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

# Define colors for neopixels
Color_Red_Bright = (255, 0, 0)
Color_Orange_Dim = (25, 3, 0)
Color_Orange_Bright = (255, 30, 0)
Color_Blue_Bright = (0, 25, 255)
Color_Blue_Dim = (0, 0, 25)
Color_Teal_Bright = (25,25,255)


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



def playRandomOrangeAnimation():
    global Color_Orange_Bright, Color_Orange_Dim, Color_Red_Bright
    Color_Orange_Bright = modify_color(Color_Orange_Bright)
    #Color_Orange_Dim = modify_color(Color_Orange_Dim)
    Color_Red_Bright = modify_color(Color_Red_Bright)

    FWD_Pixel[0] = (255, 30, 0) #Orange
    roll = random.randint(0,2)
    if roll == 0:
        OrangePortalAnim1()
    if roll == 1:
        OrangePortalAnim2()
    if roll == 2:
        OrangePortalAnim3()


def playRandomBlueAnimation():
    global Color_Blue_Bright, Color_Blue_Dim, Color_Teal_Bright
    Color_Blue_Bright =modify_color(Color_Blue_Bright)
    #Color_Blue_Dim =modify_color(Color_Blue_Dim)
    Color_Teal_Bright =modify_color(Color_Teal_Bright)

    FWD_Pixel[0] = (0, 0, 255) #Blue
    roll = random.randint(0,2)
    if roll == 0:
        BluePortalAnim1()
    if roll == 1:
        BluePortalAnim2()
    if roll == 2:
        BluePortalAnim3()


###############################################
        

# Define animation function
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

def power_on_animation():
    tuner = 50
    FWD_Pixel
    for brightness in range(0, 4):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (brightness*tuner, 0, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (brightness*tuner, 0, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation

    for brightness in range(4, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (brightness*tuner, 0, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (brightness*tuner, 0, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(0, 4):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, brightness*tuner, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,brightness*tuner, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation

    for brightness in range(4, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, brightness*tuner, 0)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,brightness*tuner, 0)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    for brightness in range(0, 4):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, 0, brightness*tuner)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,0,brightness*tuner)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation

    for brightness in range(4, -1, -1):
        for i in range(NUM_PIXELS):
            AFT_Pixel[i] = (0, 0, brightness*tuner)  # Set all pixels to current brightness
        AFT_Pixel.show()
        FWD_Pixel[0] = (0,0,brightness*tuner)
        time.sleep(0.0001)  # Adjust this value to change the speed of the animation
    brightness=1


###############################################################
###########Setup Function (Runs once on powerup)###############
###############################################################     
         
 #Initialize for audio playback
pygame.init()
#Initialize buttons
BlueButton = Button(17,bounce_time=0.1)
OrangeButton = Button(15,bounce_time=0.1)
#Initialize LEDs
FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1) 
AFT_Pixel = neopixel.NeoPixel(board.D18, 31, brightness=1) #There is actually only 29, but for animations, I am adding an extra 2 LEDs.

playRandomAudioFile("P") #Startup Sound
power_on_animation() #Neopixel Startup
playRandomAudioFile("P") #Startup Sound
print("Setup Complete, Starting Loop")

###############################################################
#####################Loop Function#############################
###############################################################

while True:
    #Wait for a button to be pressed, (using when_released since using NC button pin)
    BlueButton.when_released = callback_BlueButton_Pressed
    OrangeButton.when_released = callback_OrangeButton_Pressed
    pause()


