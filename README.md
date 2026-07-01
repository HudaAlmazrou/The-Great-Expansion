# The Great Expansion

## Overview

**The Great Expansion** is a Python-based project that visualizes the historical expansion stages of the Holy Haram by progressively drawing edge representations of historical images. The entire animation pipeline, from image preprocessing to video generation, is implemented in Python.

The project follows these main steps:

1. **Edge Extraction:** Original images representing different expansion stages are processed using Canny edge detection to preserve the most significant visual features.
2. **Pixel Extraction:** The coordinates of all edge pixels are extracted and stored as text files.
3. **Frame Generation:** The extracted pixels are drawn progressively to create a smooth animation that reveals each expansion stage in chronological order.
4. **Video Compilation:** The generated frames are combined into the final MP4 video.

---

## Project Structure

| File | Description |
|------|-------------|
| `img_to_edges.py` | Converts the original images into edge images using Canny edge detection. |
| `get_pixels.py` | Extracts edge pixel coordinates and saves them as text files. |
| `draw_img.py` | Generates animation frames by progressively drawing the extracted pixels. |
| `img_2_video.py` | Combines the generated frames into the final MP4 video. |

---

## Pipeline

To recreate the animation from scratch, execute the scripts in the following order:

### 1. Generate Edge Images

Run:

```bash
python img_to_edges.py
```

Place all source images inside the `images/` directory before running the script.

---

### 2. Extract Edge Pixels

Run:

```bash
python get_pixels.py
```

This script reads the images from the `edges/` directory and generates text files containing the pixel coordinates.

---

### 3. Generate Animation Frames

Run:

```bash
python draw_img.py
```

This script progressively draws the extracted pixels and saves the generated frames into the `try1/` directory.

---

### 4. Create the Final Video

Run:

```bash
python img_2_video.py
```

The script compiles all generated frames into the final MP4 video.

---

## Demo

🎥 **Watch the final animation on YouTube**

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube)](https://www.youtube.com/watch?v=2LPfS_yeRvc)

Or visit the video directly:

https://www.youtube.com/watch?v=2LPfS_yeRvc

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Install the required packages using:

```bash
pip install opencv-python numpy
```
