#!/usr/bin/env python3

#Made by Ranil Ganlath 04-02-2024.
#This script is used to launch other python scripts. It is used in conjunction with portalgun.desktop. 
#To install portalgun.desktop, simply copy it from this folder over to: /etc/xdg/autostart/portalgun.desktop

import subprocess
import os

# Path to the Python script (Change this to point to the latest build)
script_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Test Scripts/8PBwNPAwVP.py"


if os.getenv('DISPLAY'):
    #If we are using the graphical user interface (boot to raspi-desktop), opens new terminal
    command = f'sudo lxterminal --title="Portal Gun" --geometry=80x20 -e python3 "{script_path}"'
    subprocess.run(command, shell=True) 

else:
    #If we are using the command line interface (boot to terminal), runs script in current terminal
    command = ['sudo', 'python3', script_path]
    subprocess.run(command)
