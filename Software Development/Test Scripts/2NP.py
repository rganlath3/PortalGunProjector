#!/usr/bin/env python3

#2 NeoPixel
#Made by Ranil Ganlath 02-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#NeoPixel Test


import time
import board
import neopixel

FWD_Pixel = neopixel.NeoPixel(board.D21, 1, brightness=1)
AFT_Pixel = neopixel.NeoPixel(board.D18, 1, brightness=1)

FWD_Pixel[0] = (0, 0, 255); #Blue
AFT_Pixel[0] = (255, 30, 0); #Orange
