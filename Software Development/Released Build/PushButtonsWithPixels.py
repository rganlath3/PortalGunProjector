import time
import board
import neopixel
from gpiozero import Button
from signal import pause


#Wire Up NeoPixels and Buttons to 5V.


def callback_BlueButton_Pressed():
    print("Shooting Blue Portal!")
    FWD_Pixel[0] = (0, 0, 255); #Blue
    AFT_Pixel[0] = (0, 0, 255); #Blue

def callback_OrangeButton_Pressed():
    print("Shooting Orange Portal!")
    FWD_Pixel[0] = (255, 30, 0); #Orange
    AFT_Pixel[0] = (255, 30, 0); #Orange


BlueButton = Button(17) #Blue Pushbutton
OrangeButton = Button(15) #Orange Pushbutton

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1)
AFT_Pixel = neopixel.NeoPixel(board.D18, 1, brightness=1)


while True:

#Using Released due to pullup resistor
    BlueButton.when_released = callback_BlueButton_Pressed
    OrangeButton.when_released = callback_OrangeButton_Pressed
    pause()
























