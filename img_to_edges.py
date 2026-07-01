import cv2
import os

image_paths = os.listdir("images")

for image_path in image_paths:
    img = cv2.imread("images/"+image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite("edges/edge_"+image_path.split(".")[0]+".png", edges)



