#!/usr/bin/env python3

#Made by Ranil Ganlath 03-2024.
#This script is used for Ranil's Portal Gun Projector Project and contains the following features:
#Audio File Counter

import subprocess

# AUDIO PART
global AudioPath #Stores Audio Directory Folder Path
R_count = 6 #Store number of R_.wav files in Audio Directory
B_count = 6 #Store number of B_.wav files in Audio Directory
P_count = 7 #Store number of P_.wav files in Audio Directory
A_count = 2 #Store number of R_.wav files in Audio Directory
M_count = 5 #Store number of B_.wav files in Audio Directory
T_count = 5 #Store number of P_.wav files in Audio Directory
#Find Audio Directory
AudioPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Sounds/"

#DEVELOPER note I should hardcode these values in to save on startup time.
#Now we count how many of each type of file is in this audio directory to dynamically adjust to new sound files added.
# Get the list of files in the directory that contain a letter like 'R'
result = subprocess.run(['ls', AudioPath], stdout=subprocess.PIPE, universal_newlines=True)
R_count = len([filename for filename in result.stdout.split() if 'R' in filename])
B_count = len([filename for filename in result.stdout.split() if 'B' in filename])
P_count = len([filename for filename in result.stdout.split() if 'P' in filename])
A_count = len([filename for filename in result.stdout.split() if 'A' in filename])
M_count = len([filename for filename in result.stdout.split() if 'M' in filename])
T_count = len([filename for filename in result.stdout.split() if 'T' in filename])




print("R_Count = ", R_count)
print("B_Count = ", B_count)
print("P_Count = ", P_count)
print("A_Count = ", A_count)
print("M_Count = ", M_count)
print("T_Count = ", T_count)
