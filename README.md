# The Great Expansion

## Overview
هو العمل ده بالكامل اتعمل باستخدام لغة البايثون بالخطوات دي بالترتيب:
١- حولنا كل صور المراحل بتاعة توسيع الحرم ل edge image وده بيتم عن طريق تطبيق فلتر علي الصوره وال edge image دي عباره عن صوره بيبقي فيها التفاصيل المهمه الي في الصوره زي ما هو واضح في الفديو
٢- بعد كده باستخدام البايثون برضه اتحكمنا في ظهور ال edge image دي بحيث انها تظهر بالتريج وبالترتيب بتاع المراحل

---

## Project Files
* `img_to_edges.py`: Applies a Canny edge detection filter to the original images.
* `get_pixels.py`: Extracts the pixel coordinates from the edge images and saves them to text files.
* `draw_img.py`: Reads the pixel coordinates and creates a sequential animation of the edges drawing themselves.
* `img_2_video.py`: Compiles the generated sequence of images into the final `.mp4` video.

---

## How to Generate the Video
To recreate "The Great Expansion" video from scratch, run the Python scripts in the following exact order:

1. [cite_start]**Generate Edge Images:** Convert images to edges using `img_to_edges.py` code[cite: 1]. Ensure your source images are placed in an `images/` directory before running.
2. [cite_start]**Extract Pixel Data:** Use `get_pixels.py` to generate txt files[cite: 2]. This will read from the `edges/` directory and output `.txt` files containing the pixel coordinates.
3. [cite_start]**Animate the Frames:** Use `draw_img.py` to generate images that will appear on the video[cite: 3]. This script will output a large sequence of frames into a `try1/` directory. (Note: This process may take some time depending on the number of pixels).
4. [cite_start]**Compile the Video:** Use `img_2_video.py` to generate the final video[cite: 4]. This will read the frames from the `try1/` folder and output the final video file.
