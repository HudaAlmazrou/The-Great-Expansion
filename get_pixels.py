import cv2
import os


#12 -> 2
#10, 11 -> 1.05

#6,7,8,9 -> 1.25
#1,2,3,4,5 -> 1.5
for k in range(1,13):
    img = cv2.imread("edges/edge_BLACK_"+str(k)+".png")

    h,w,_ = img.shape
    if k<6:
        img = cv2.resize(img, (int(1.5*w), int(1.5*h)))
    elif k<10:
        img = cv2.resize(img, (int(1.25 * w), int(1.25 * h)))
    elif k<12:
        img = cv2.resize(img, (int(1.05 * w), int(1.05 * h)))
    else:
        img = cv2.resize(img, (int(2 * w), int(2 * h)))
    h, w, _ = img.shape

    file = open("edge_BLACK_"+str(k)+".txt", "w")
    for i in range(h):
        for j in range(w):
            if img[i,j,0] != 0:
                file.write(str(j)+"\t"+str(i)+"\n")

    file.close()


