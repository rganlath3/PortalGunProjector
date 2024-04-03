#!/usr/bin/env python3

#1 PushButton
#Made by Ranil Ganlath 02-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#PushButton Support

from gpiozero import Button
from signal import pause


def callback_BlueButton_Pressed():
    print("Shooting Blue Portal!")

def callback_OrangeButton_Pressed():
    print("Shooting Orange Portal!")


BlueButton = Button(17) #Blue Pushbutton
OrangeButton = Button(15) #Orange Pushbutton

#Using Released due to pullup resistor
BlueButton.when_released = callback_BlueButton_Pressed
OrangeButton.when_released = callback_OrangeButton_Pressed

pause()