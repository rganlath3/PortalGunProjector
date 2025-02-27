# Portal Gun Embedded Projector

[![Hardware License: CERN-OHL-S-2.0](https://img.shields.io/badge/Hardware%20License-CERN--OHL--S--2.0-lightgrey.svg)](https://ohwr.org/cern_ohl_s_v2.txt)
[![Software License: GPL v3](https://img.shields.io/badge/Software%20License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Status: In Development](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()


A Portal Gun prop featuring an embedded HDMI projector that displays authentic Portal visuals and sounds. This project combines 3D printing, electronics, and software to create a realistic prop that doubles as a portable projector. The portal gun is from popular Valve videogame, Portal / Portal 2.

![Portal Gun Iso View](/VisualDocumentation/CAD-ISO_View_1.png)

<!-- TABLE OF CONTENTS -->
## Table of Contents

<details>
<summary>Table of Contents</summary>

1. [About The Project](#about-the-project)
    - [Design Tools & Requirements](#design-tools--requirements)
        - [Software Requirements](#software-requirements)
        - [Hardware Requirements](#hardware-requirements)
2. [Hardware Development](#hardware-development)
    - [Bill of Materials](#bill-of-materials)
    - [Hardware Used](#hardware-used)
    - [3D Printing the Model](#3d-printing-the-model)
    - [3D Printing Specifications](#3d-printing-specifications)
    - [Model Prep](#model-prep)
    - [Electrical Interconnect Diagram](#electrical-interconnect-diagram)
    - [PCB](#pcb)
    - [Wiring](#wiring)
    - [Power](#power)
3. [Software Development](#software-development)
4. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Common Issues](#common-issues)
5. [Assets](#assets)
    - [Audio](#audio)
    - [Video](#video)
6. [Roadmap](#roadmap)
7. [Contributing & Donations](#contributing--donations)
8. [License](#license)
9. [Contact](#contact)

</details>


<!-- ABOUT THE PROJECT -->
## About The Project
The idea was to take 3D printing a Portal Gun Prop to the next level of realism. My brother inspired me to create a Prop Portal Gun with an full HDMI Projector inside of the prop. When activated, it displays authentic Portal visuals, produces game-accurate sound effects through integrated speakers, and displays LED effects. The project combines 3D printing, electronics, and software development to create a prop that's both visually accurate and practically useful as a portable projector.

### Design Tools & Requirements

#### Software Requirements
- Python 3.9+ (Programming Language for RPi)
- Raspberry Pi OS Debian v12 (64-bit)
- VS Code (Programming IDE)
- Autodesk Fusion360 (Free CAD Software)
- KiCAD 7 (Open Source PCB Design Software)
- Ultimaker Cura (Free 3D Slicing Software)

#### Hardware Requirements
- Raspberry Pi 4 (8GB RAM recommended)
- 32GB+ SD Card
- 12V Power Supply or 4S Lipo Battery Pack

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Hardware Development

### Bill of Materials
Coming Soon

### Hardware Used
* Raspberry Pi 4 (SBC)
* Custom RPi HAT PCB (Power and GPIO Distribtuion to Screw Terminals) (See PCB Designs)
* Various Capacitors, Resistors, SMD LEDs, JST Connectors, Wire Crimps, etc.
* Various stranded wire lengths and colors: 16AWG, 22AWG.
* 1x DROK 9V-24V to 5V Step Down Buck Converter, 30W (Powers Pi from Battery Input)
* 1x Songhe 10-32V to 21V Step Up Boost Converter, 150W (Powers Projector from Battery Input)
* 1x 16mm Momentary Metal LED Push Button (Orange)
* 1x 16mm Momentary Metal LED Push Button (Blue)
* 2x 2.1mm DC Barrel Jacks Pair (Power Input)
* 2x SPST 20A Heavy Duty Toggle Switch (Projector Power and Pi Power)
* 1x SPST 5A Mini Toggle Switch (LED Power)
* 1x Individually Addressable 5V NeoPixel
* 1x 1ft. RGB COB Individually Addressable 5V LED Strip 
* Portal Gun 3D Design: (found on thingiverse [here](https://www.thingiverse.com/thing:3579224)) 
* My modifications to the Portal Gun 3D Design.
* 3D Printer: Creality CR-10SProV2


### 3D Printing the Model
I used this portal gun design as a basis for my version. This creator put a lot of work into his design so please give him the attention he deserves: [EVARATE Portal Gun](https://www.thingiverse.com/thing:3579224)

### 3D Printing Specifications

#### Print Settings
- Layer Height: 0.2mm
- Infill: 15% for most parts but 100% for finger parts
- Temperature: 210°C (PLA+)
- Build Plate: 60°C
- Support: Required for overhangs
- Material: eSUN PLA+ or equivalent


<img src="/VisualDocumentation/CAD-Embedding_Projector.png" width="300">


Besides modifying parts to fit the projector, I also designed an electronics sled to fit the handle base. This is what the DC-DC converters and Raspberry Pi mount to.

<img src="/VisualDocumentation/CAD-Electronics_Sled.png" width="200">


### Model Prep
Sanding, filler, painting, etc.

* 3M Acryl Putty, 05096 Green or 05098 Red
* Various Sandpaper and Sanding Sponges
* Dremel
* P95 or Better Respirator (don't cheap out on this)
* Filler & Sandable Primer (I use cheap Rust-Oleum)
* Montana Gold Shock White Pure Spray Paint
* Montana Gold Shock Black Spray Paint
* Spray Max USC 2K High Gloss Clearcoat (Automotive Clearcoat, expensive but worth it!)

Once all the parts have been printed, we need to do some post processing to get the prints as smooth as possible. For my first iteration, I used a dremel to manually cut holes in some parts instead of just CADing them out. (I wasn't sure how things would exactly fit.)

*Note: Anytime we are sanding or spray painting, you MUST be wearing that respirator! 
Also try to handle all the parts with rubber gloves so your fingerprints don't mess up the paint coats.*

<img src="/VisualDocumentation/Sanding_3D_Printed_Parts_1.jpg" width="300">


Using sanding paper and sponges I used the following grits:
120->220->320->400 using spot putty where needed. Anything above 320 grit should be wet sanded. Then 2x coats of fillable primer spray paint. Then 400 grit. Then 1x coat of fillable primer. Then one more 400 grit. Then 600 grit. Then apply desired paint color (black and white) base coat in many light coats. (3-5 coats) I'd like to try to find an alternate to Montana Gold.

<img src="/VisualDocumentation/Sanding_3D_Printed_Parts_2.jpg" width="300">


Once fully dried, use a damp sponge and wipe the parts. Use 1000 grit to sand down the base coat. 

Optional: Using citadel paints or any acrylic paints, add weathering, scuff marks, or damage. I ended up using a metal file and creating scratches. I finely dry brushed silver paint onto the black parts to create a metallic highlight effect. I also added a white line on the top white part.

Once finished painting, we can now apply layers of clearcoat in a very well ventilated area. This 2K stuff is really toxic so be careful. I ended up using rust-oleum 2x ultracover clear instead which gave a good result but not as nice as 2k would have been. I used gloss clear coat on the white parts and black arms. I used matte clear coat on the black parts. Once fully cured, assembly can begin.

### Electrical Interconnect Diagram
![Electrical Interconnect Diagram](/VisualDocumentation/Electrical-Portal_Gun_Projector_Interconnect.jpg)


### PCB
I designed a Raspberry Pi Hat PCB that handles powering the board (via 5V pins), powering LEDs, and acting as GPIO inputs/outputs for button inputs and driving neopixels. See Mk2 design for the latest. If I had a chance for another iteration, I would add slotted holes in the center section for the placement of a low profile fan for cooling the raspberry pi.

<img src="/VisualDocumentation/PCB-Iso_View.png" width="400">


### Wiring
I used 22AWG and 16AWG for all wiring in the system. 22AWG was used for neopixels and GPIO pins while 16AWG was used for all power lines. 
* Red - Power
* Black - GND
* Green - Data / GPIO

<img src="/VisualDocumentation/CAD-Cross_Section_1.png" width="700">


### Power
I have two separate power circuits: Pi and Projector.

The Pi Circuit runs on 5V. It powers the neopixels, raspberry pi, and push button LEDs.
* Input Voltage: 12V
* Converted Voltage: 5V
* Average Wattage (Script Running): 4.1W
* Theorhetical Max Load: 
* Safety Factor (Max Power * 1.25W): 7W
* Battery Required for 2 hour battery life:

The Projector Circuit runs on 21V. It powers the projector and it's internal speakers.
* Input Voltage: 12V
* Converted Voltage: 21V
* Average Watage (Lamp On): 41.46W
* Theorhetical Max Load:
* Safety Factor (Max Power * 1.25W): 53W
* Battery Required for 2 hour battery life:

<img src="/VisualDocumentation/Initial_Electroincs_Testing.jpg" width="500">


## Software Development
I am familiar using an Arduino or other MCU to solve all my hardware integration problems. In the past I've used Arduinos + Raspberry Pis when needed (such as for ROS projects). For this project, I wanted to challenge myself to not use any MCUs and to only use the raspberry pi GPIO pins to interact with switches and LED control. It brought up some fun compatibility issues that prevented me from using a Raspberry Pi 5 until libraries were updated. 

***Disclaimer: I am an electrical engineer, so apologies for the chaos that is my programming.***

<!-- GETTING STARTED -->
## Getting Started

* Install Raspberry Pi OS with Desktop (Debian v12) (64-bit)
  * we will use the desktop version for initial setup then switch to the CLI for actual operation. This saves time when troubleshooting things like VLC issues.
* Copy this repo to any desired folder. 
  * For reference, my filepath was: */home/aperture/Documents/PortalGunProjector*


### Prerequisites
*Note: Since Neopixel Usage requires root priviledges, make sure your environment path is configured accordingly. I recommend installing all these python libraries as root (sudo command). It is possible to run sudoless but it requires using only GPIO10 for LEDs*

```bash
# Update System
sudo apt update && sudo apt upgrade -y

# Install Required Packages
sudo apt install git python3-pip vlc -y


# Install Python Dependencies

# Raspberry PI GPIO Control
sudo pip3 install gpiozero

# NeoPixel Drivers
sudo pip3 install adafruit-circuitpython-neopixel

# Pygame
sudo pip3 install pygame

# VLC
sudo apt install vlc

# VLC Python Bindings
sudo pip3 install python-vlc
```


### Installation

1. If you haven't already, clone the repo, to a directory such as: */home/username/Documents/PortalGunProjector*

   ```sh
   git clone https://github.com/rganlath3/PortalGunProjector.git
   ```
2. Install prequisites listed above.

3. Run each test script to test functionality as you build, then run launch.py


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Common Issues

1. LED Control Fails
```bash
# Check permissions
sudo usermod -a -G gpio $USER
# Reboot required after permission change
```

2. Video Playback Issues
- Ensure micro HDMI port used is closest to USB-C power connector.
- Check video codec compatibility
- Verify file permissions

## Assets

### Audio
The portal gun plays audio out of the hdmi audio output via the projector speakers. Everytime a button is pressed, a random soundclip from a list will play to add some variety to mashing buttons. All audio files are in the "Sounds" folder and are extracted from in game. I do not own these files.

### Video
On bootup a random video and audio line will play as an initialization. On button presses, a random sized orange or blue portal video will play on loop. I manually created these videos by screen recording Garry's Mod and careful editing. Bootup videos are sourced from Portal Gameplay and Trailers from Value and are not owned by me. 


<!-- ROADMAP -->
## Roadmap
- [x] CAD Small Projector
- [x] Modify Portal Gun Designs
- [x] Design electrical interconnect
- [x] 3D Print all parts
- [x] Sanding and post processing on parts
- [x] Painting all parts
- [x] Redesign electrical interconnect
- [x] Create Electronics Sled
- [x] Create wiring harness
- [x] Test LED effects
- [x] Integrate pushbuttons into programming
- [x] Create portal and bootup videos
- [x] Configure code to run on startup
- [x] Add Visual Documentation to GitHub
- [x] Assemble Portal Gun
- [x] Final tests with benchtop power supply
- [ ] Add magnets and external cables
- [ ] Create Battery Harness

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing & Donations

Any donation helps to support parts for future open source projects!
[Buy Me a Coffee ☕](https://www.buymeacoffee.com/rganlath)

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License
The contents of this project itself is licensed under CERN-OHL-S-2.0 and the underlying source code used for programming the raspberry pi is licensed under GNU GPLv3. Both of these licenses require attribution.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ranil Ganlath - ranil.ganlath@gmail.com

Project Link: [https://github.com/rganlath3/PortalGunProjector](https://github.com/rganlath3/PortalGunProjector)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
