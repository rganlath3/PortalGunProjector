
#video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP0.mp4"  # Update with your video file path

#04-03-2024
#This works in command line but has a slight lag when looping video. I'm looking for alternatives.
#vlc "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP1.mp4" --loop --no-video-title --fullscreen --no-qt-fs-controller

#This attempt uses OpenCV to run videos.
import cv2

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the width and height of the video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width)
    print(height)
    # Create a window
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # Read a frame
        ret, frame = cap.read()

        # Check if the frame is empty (end of video)
        if not ret:
            # Reset to the beginning of the video
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Display the frame
        cv2.imshow("Video", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    # Path to the video file
    video_path = "/home/aperture/Documents/PortalGunProjector/Software Development/Videos/BP3.mp4"  # Update with your video file path

    play_video(video_path)
