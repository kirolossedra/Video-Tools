import cv2
import os

# Function to extract all frames (30 frames per second)
def extract_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
    
    # Get the original frames per second (FPS) of the video
    original_fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_duration = total_frames / original_fps
    
    print(f"Original FPS: {original_fps}")
    print(f"Total Frames: {total_frames}")
    print(f"Video Duration: {video_duration} seconds")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_count = 0
    saved_frame_count = 0
    
    while True:
        # Read a frame
        ret, frame = video.read()
        
        # If no more frames, exit
        if not ret:
            break
        
        # Save every frame
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        print(f"Saved: {frame_path}")
        frame_count += 1

    # Release the video capture object
    video.release()
    print(f"Total frames saved: {frame_count}")

# Example usage
video_path = 'vid/input.mp4'  # Your MP4 video file
output_folder = 'frames_output'  # Directory to save frames

extract_frames(video_path, output_folder)
