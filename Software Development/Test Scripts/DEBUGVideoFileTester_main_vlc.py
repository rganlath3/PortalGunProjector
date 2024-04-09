from gpiozero import Button
from signal import pause
import vlc
import random

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

print(len(video_files))



# creating a media player object 
media_player = vlc.MediaListPlayer() 
media_player.set_playback_mode(2) #This works, this loops whatever the current video in queue is. Maybe now we just have buttons that change index.

# creating Instance class object 
player = vlc.Instance() 
# creating a new media list object 
media_list = player.media_list_new() 
  

for video in range(len(video_files)):
    media = player.media_new(VideoPath+video_files[video]) # creating a new media 
    media_list.add_media(media) # adding media to media list 
    media_player.set_media_list(media_list) # setting media list to the media player 
    
""" 
#Turn this into a for loop later
media = player.media_new(VideoPath+"BP1.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 
  
media = player.media_new(VideoPath+"BP2.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 

media = player.media_new(VideoPath+"BP3.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 

media = player.media_new(VideoPath+"BP4.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 

media = player.media_new(VideoPath+"OP1.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 
  
media = player.media_new(VideoPath+"OP2.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 

media = player.media_new(VideoPath+"OP3.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 

media = player.media_new(VideoPath+"OP4.mp4") # creating a new media 
media_list.add_media(media) # adding media to media list 
media_player.set_media_list(media_list) # setting media list to the media player 
#END FOR LOOP
 """



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
