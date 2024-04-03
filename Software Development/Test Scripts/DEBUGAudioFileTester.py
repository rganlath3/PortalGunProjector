#!/usr/bin/env python3

#Made by Ranil Ganlath 03-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#Audio Tester

from signal import pause
import pygame


# AUDIO SETUP
AudioPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Sounds/"
R_count = 6 #Store number of R_.wav files in Audio Directory
B_count = 6 #Store number of B_.wav files in Audio Directory
P_count = 9 #Store number of P_.wav files in Audio Directory
A_count = 2 #Store number of R_.wav files in Audio Directory
M_count = 6 #Store number of B_.wav files in Audio Directory
T_count = 5 #Store number of P_.wav files in Audio Directory
pygame.init()

DesiredFileName = "T1"


pygame.mixer.Sound(AudioPath+DesiredFileName+".wav").play()
while True:
    pause()