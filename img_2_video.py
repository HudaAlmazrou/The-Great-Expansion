import cv2
import glob
import numpy as np


# Path to the folder containing images
image_folder = 'try1'
video_name = 'try3.mp4'

# Get a list of image files (sorted by name)
images = sorted(glob.glob(f"{image_folder}/*.png"))  # Use *.png, *.jpeg, etc. based on your images

# Check if there are images in the folder
if not images:
    print("No images found in the folder.")
    exit()

# Get the dimensions of the first image
frame = cv2.imread(images[0])
height, width, layers = frame.shape

# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))  # 30 is the frame rate (can be adjusted)

# Write each image to the video
for image in images:
    frame = cv2.imread(image)
    video.write(frame)

# Release the VideoWriter
video.release()

print("Video created successfully!")
