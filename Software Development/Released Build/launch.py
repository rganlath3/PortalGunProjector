#!/usr/bin/env python3

#Made by Ranil Ganlath 04-02-2024.
#This script is used to launch other python scripts. It is used in conjunction with portalgun.desktop. 
#To install portalgun.desktop, simply copy it from this folder over to: /etc/xdg/autostart/portalgun.desktop

import subprocess

command = 'sudo lxterminal --title="Portal Gun" --geometry=80x20 -e python3 "/home/aperture/Documents/PortalGunProjector/Software Development/Test Scripts/PushButtonsWithPixelAnimationsWithSoundsImproved.py"'
#command = 'sudo lxterminal --title="Portal Gun" --geometry=800x800 -e python3 "/home/aperture/Documents/PortalGunProjector/Software Development/Test Scripts/PushButtonsWithPixelAnimationsWithSoundsImproved.py"'

subprocess.run(command, shell=True)