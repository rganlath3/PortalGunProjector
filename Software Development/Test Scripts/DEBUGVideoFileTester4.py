from gpiozero import Button
from signal import pause
import vlc
import time




playlist = ["/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP3.mp4","/home/aperture/Documents/PortalGunProjector/Software Development/Videos/OP3.mp4"]



""" 
    def addPlayList(self, localPath):
        self.mediaList = self.player.media_list_new()
        path = os.path.join(os.getcwd(), localPath)
        self.mediaList.add_media(path)
        self.listPlayer = self.player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.set_playback_mode(vlc.PlaybackMode(1))
 """
for song in playlist:
    player = vlc.MediaPlayer(song)
    player.vlm_set_loop("BP3", True) 
    #player.PlaybackMode(1)
    player.play()




def playVideo(video_path):
    print("Test")

def playVideoBlue():
    video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP3.mp4"
    playVideo(video_path)

def playVideoOrange():
    video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/OP3.mp4"
    playVideo(video_path)

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

print("Setup Complete, Ready for Portals")

pause()
