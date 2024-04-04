# This launches a video and opens a remote, you can type "next" into it. I recommend doing this on a new terminal:
# vlc "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP1.mp4" --repeat --one-instance -I rc

#This adds a video to the playlist.
#vlc "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/OP1.mp4" --loop --playlist-enqueue --one-instance

#After adding a video to the playlist, type skip and then clear the playlist besides the current item.



from gpiozero import Button
from signal import pause
import subprocess
import queue

# Global variables
video_queue = queue.Queue()
current_process = None

def playVideo(video_path):
    global current_process
    # Play the video
    cmd = ["vlc", "--fullscreen", video_path]
    current_process = subprocess.Popen(cmd)

def playNextVideo():
    global current_process
    # Check if there are videos in the queue
    if not video_queue.empty():
        next_video = video_queue.get()
        # Send a command to VLC to play the next video
        if current_process:
            cmd = ["vlc", "--control", "enqueue", next_video]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def playVideoBlue():
    video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP3.mp4" 
    video_queue.put(video_path)
    playNextVideo()

def playVideoOrange():
    video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/OP3.mp4" 
    video_queue.put(video_path)
    playNextVideo()

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
video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/OP4.mp4" 
playVideo(video_path)
pause()
