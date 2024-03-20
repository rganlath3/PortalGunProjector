import board
import neopixel
from gpiozero import Button
from signal import pause
import pygame
# Wire Up NeoPixels and Buttons to 5V.

def callback_BlueButton_Pressed():
    global blue_active
    if not blue_active:
        print("Shooting Blue Portal!")
        setAllBlueStatic()
        blue_active = True
        orange_active = False

def callback_OrangeButton_Pressed():
    global orange_active
    if not orange_active:
        print("Shooting Orange Portal!")
        setAllOrangeStatic()
        orange_active = True
        blue_active = False

def setAllOrangeStatic():
    beep.play()
    FWD_Pixel[0] = (255, 30, 0)  # Orange
    for x in range(0, 28):
        AFT_Pixel[x] = (255, 30, 0)

def setAllBlueStatic():
    FWD_Pixel[0] = (0, 0, 255)  # Blue
    for x in range(0, 28):
        AFT_Pixel[x] = (0, 0, 255)

blue_active = False
orange_active = False


pygame.init()
beep = pygame.mixer.Sound("/home/aperture/PortalGunProjector/Software Development/Audio Assets/beepclear.wav")
blue_button = Button(17)  # Blue Pushbutton
orange_button = Button(15)  # Orange Pushbutton

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1)
AFT_Pixel = neopixel.NeoPixel(board.D18, 29, brightness=1)

# Assign callbacks
blue_button.when_pressed = callback_BlueButton_Pressed
orange_button.when_pressed = callback_OrangeButton_Pressed

pause()
