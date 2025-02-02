# Portal Gun Embedded Projector

![Alt text](/VisualDocumentation/CAD - ISO View.png)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#assets">Assets</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A projector embedded into a sci fi 3D printed gun from the popular Valve Game, Portal.

The idea was to take 3D printing a portal gun on thingiverse to the next level of realism. My brother inspired me to create a portal gun with an actual hdmi projector inside of the gun. This projector was project visuals from the game and act as a standard portable projector. Alongside portal visuals, the gun needed to produce sounds (and constant ambient audio) and control two sets of led neopixels. Power distribution and button wiring also needs to be managed inside the gun. The only external features besides interfaces button are two DC jacks that feed to batteries or wall power. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Software Design Tools

* Python (Primary Programming Language for this project)
* VS Code (Programming IDE)
* Fusion360 (Free CAD Software)
* KiCAD 7 (Free PCB Design Software)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Hardware Development

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
* 3D Printer (I used eSUN PLA+ Filament for all parts) (not a sponser, use whatever you like)


### 3D Printing the Model
Slicer settings

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

Using sanding paper and sponges I used the following grits:
120->220->320->400 using spot putty where needed. Anything above 320 grit should be wet sanded. Then 2x coats of fillable primer spray paint. Then 400 grit. Then 1x coat of fillable primer. Then one more 400 grit. Then 600 grit. Then apply desired paint color (black and white) base coat in many light coats. (3-5 coats)

Once fully dried, use a damp sponge and wipe the parts. Use 1000 grit to sand down the base coat. 

Optional: Using citadel paints or any acrylic paints, add weathering, scuff marks, or damage. I ended up using a metal file and creating scratches. I finely dry brushed silver paint onto the black parts to create a metallic highlight effect. I also added a white line on the top white part.

Once finished painting, we can now apply layers of clearcoat in a very well ventilated area. This 2K stuff is really toxic so be careful. I ended up using rust-oleum 2x ultracover clear instead which gave a good result but not as nice as 2k would have been. I used gloss clear coat on the white parts and black arms. I used matte clear coat on the black parts. Once fully cured, assembly can begin.

### PCB
I designed a Raspberry Pi Hat PCB that handles powering the board (via 5V pins), powering LEDs, and acting as GPIO inputs/outputs for button inputs and driving neopixels. See Mk2 design for the latest. If I had a chance for another iteration, I would add slotted holes in the center section for the placement of a low profile fan for cooling the raspberry pi.

### Wiring
I used 22AWG and 16AWG for all wiring in the system. 22AWG was used for neopixels and GPIO pins while 16AWG was used for all power lines. 
* Red - Power
* Black - GND
* Green - Data / GPIO

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


## Software Development
I am so used to using an arduino or other MCU to solve all my hardware integration problems. In the past I've used arduinos + raspberry pis when needed (such as for ROS projects). For this project, I wanted to challenge myself to not use any MCUs and to only use the raspberry pi GPIO pins to interact with switches and LED control. It definitely brought up some fun issues discussed in detail below but taught me a lot.

***Disclaimer: I am an electrical engineer, so apologies for the chaos that is my programming.***

<!-- GETTING STARTED -->
## Getting Started

* Install Raspberry Pi OS with Desktop (Debian v12) (64-bit)
  * we will use the desktop version for initial setup then switch to the CLI for actual operation. This saves time when troubleshooting things like VLC issues.
* Copy this repo to any desired folder. 
  * For reference, my filepath was: */home/aperture/Documents/PortalGunProjector*


### Prerequisites
*Note: Since Neopixel Usage requires root priviledges, make sure your environment path is configured accordingly. I recommend installing all these python libraries as root (sudo command). It is possible to run sudoless but it requires using only GPIO10 for LEDs*

* Raspberry PI GPIO Control
  ```sh
  sudo pip3 install gpiozero
  ```
* neopixel drivers
  ```sh
  sudo pip3 install adafruit-circuitpython-neopixel
  ```
* pygame
  ```sh
  sudo pip3 install pygame
  ```
* vlc
  ```sh
  sudo apt install vlc
  ```
* vlc python bindings
  ```sh
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

## Assets

### Audio
The portal gun plays audio out of the hdmi audio output via the projector speakers. Everytime a button is pressed, a random soundclip from a list will play to add some variety to mashing buttons. All audio files are in the "Sounds" folder and are recorded from in game. I do not own these files.

### Video
On bootup a random video and audio line will play as an initialization. On button presses, a random sized orange or blue portal video will play. I manually created these videos by screen recording Garry's Mod and careful editing. Bootup videos are sourced from Portal Gameplay and Trailers from Value off the internet and are not owned by me. 


<!-- ROADMAP -->
## Roadmap

- [ ] Add Visual Documentation to GitHub
- [x] Paint Parts
- [x] Assemble Parts
- [ ] Create Battery Harness and Holder


See the [open issues](https://github.com/rganlath3/PortalGunProjector/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ranil Ganlath - ranil.ganlath@gmail.com

Project Link: [https://github.com/rganlath3/PortalGunProjector](https://github.com/rganlath3/PortalGunProjector)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
