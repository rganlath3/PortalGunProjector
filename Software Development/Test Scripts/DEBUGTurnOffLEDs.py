#!/usr/bin/env python3

#2 NeoPixel
#Made by Ranil Ganlath 02-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#NeoPixel Test


import time
import board
import neopixel

Color_White = (255, 255, 255)
Color_OFF = (0,0,0)

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1) 
AFT_Pixel = neopixel.NeoPixel(board.D18, 31, brightness=1) #There is actually only 29, but for animations, I am adding an extra 2 LEDs.


FWD_Pixel.fill(Color_OFF)
AFT_Pixel.fill(Color_OFF)

#FWD_Pixel.fill(Color_White)
#AFT_Pixel.fill(Color_White)