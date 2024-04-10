#from signal import pause
import vlc
#import time
import pathlib


#Find Audio Directory
#Using Pathlib, we can navigate to the audio directory regardless of how we start this script and regardless of where the shagohod directory is stored.
VideoPath = str(pathlib.Path(__file__)) #get the file path where this script is stored. Ex. /home/sokolov/shagohod/ROS/catkin_ws/src/granin/scripts/
index = VideoPath.rfind("PortalGunProjector")
if index != -1:
    VideoPath = VideoPath[:index + len("PortalGunProjector")] + "/Software Development/Videos/"
else:
    print("Can't find video path")
print(VideoPath)

playlist = ["x:/zenta/Documents/GitHub/PortalGunProjector/Software Development/Videos/BP3.mp4"]

#print(playlist)


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
    #player.vlm_set_loop("BP3", True) 
    #player.PlaybackMode(1)
    player.play()
    print("Huh?")




def playVideo(new_path):
    print("Test")

def playVideoBlue():
    new_path = VideoPath+"BP3.mp4"
    playVideo(new_path)

def playVideoOrange():
    new_path = VideoPath+"OP3.mp4"
    playVideo(new_path)

def callback_BlueButton_Pressed():
    playVideoBlue()

def callback_OrangeButton_Pressed():
    playVideoOrange()

