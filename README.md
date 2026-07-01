# The Great Expansion

## Overview
This entire project was built completely using Python, executing the following steps in sequence:
1. All source images representing the expansion stages of the Holy Haram were converted into edge images. This was achieved by applying a filter to the images, isolating and highlighting the most critical details as shown in the video.
2. Using Python, the gradual visibility and sequential progression of these edge images were controlled to display the stages in chronological order.

---

## Project Files
* `img_to_edges.py`: Applies a Canny edge detection filter to the original images.
* `get_pixels.py`: Extracts the pixel coordinates from the edge images and saves them to text files.
* `draw_img.py`: Reads the pixel coordinates and creates a sequential animation of the edges drawing themselves.
* `img_2_video.py`: Compiles the generated sequence of images into the final `.mp4` video.

---

## How to Generate the Video
To recreate "The Great Expansion" video from scratch, run the Python scripts in the following exact order:

1. **Generate Edge Images:** Convert images to edges using `img_to_edges.py` code. Ensure your source images are placed in an `images/` directory before running.
2. **Extract Pixel Data:** Use `get_pixels.py` to generate txt files. This will read from the `edges/` directory and output `.txt` files containing the pixel coordinates.
3. **Animate the Frames:** Use `draw_img.py` to generate images that will appear on the video. This script will output a large sequence of frames into a `try1/` directory.
4. **Compile the Video:** Use `img_2_video.py` to generate the final video. This will read the frames from the `try1/` folder and output the final video file.

---

## Result
* [Output Video]([https://www.youtube.com/watch?v=9a1oRKIi104](https://www.youtube.com/watch?v=2LPfS_yeRvc))
