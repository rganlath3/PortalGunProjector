from gpiozero import Button
from signal import pause
import vlc
import random

#See this link for more info on vlc https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Instance-class.html

# VIDEO SETUP
VideoPath = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/"
VBP_count = 4 #Store number of BP_.wav files in Audio Directory
VOP_count = 4 #Store number of OP_.wav files in Audio Directory


#Path Setup
video_files = []
for file in range(1,VBP_count+1):
    video_files.append("BP"+str(file)+".mp4")
for file in range(1,VOP_count+1):
    video_files.append("OP"+str(file)+".mp4")

#at this point, the array is fully built, now let's iterate over it after creating our media players


# creating Instance class object 
player = vlc.Instance() 

# Create a media player object
playman = vlc.MediaPlayer()
playman.set_fullscreen(True)
playman.audio_set_track(-1) #disable audio

# creating a media list player object 
media_player = vlc.MediaListPlayer() 
media_player.set_playback_mode(2) #repeat current video

# creating a new media list object 
media_list = player.media_list_new() 

#Add all videos to playlist
for video in range(len(video_files)):
    media = player.media_new(VideoPath+video_files[video]) # creating a new media 
    media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 
media_player.set_media_player(playman)



#Description
#Function that puts all the portal videos into a big playlist.
# Ex. Blue Portal 1-4 are index 0 to 3. Orange Portal 1-4 are index 4-7
#Then when a button is pushed, we tell the media_player to play the item at that index (can be randomized)



def playVideo(desiredIndex):
    media_player.play_item_at_index(desiredIndex) 

def playVideoBlue():
    playVideo(random.randint(0,3))

def playVideoOrange():
    playVideo(random.randint(4,7))

def callback_BlueButton_Pressed():
    playVideoBlue()

def callback_OrangeButton_Pressed():
    playVideoOrange()

# Initialize buttons
BlueButton = Button(17,bounce_time=0.1)
OrangeButton = Button(15,bounce_time=0.1)

# Assign button callbacks
BlueButton.when_released = callback_BlueButton_Pressed
OrangeButton.when_released = callback_OrangeButton_Pressed

#Initial Bootup Video
playVideo(0)
print("Setup Complete, Ready for Portals")
pause()
