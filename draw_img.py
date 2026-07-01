import cv2
import random
import numpy as np


file = open("edge_BLACK_"+str(1)+".txt", "r")

img = np.zeros((1080,1280))

lines = file.readlines()
all_pixels = []
for line in lines:
    line = line.split()
    all_pixels.append([640,540, int(line[0])-int(1.5*58)+640, int(line[1])-int(1.5*53)+540])

count = 1000000
print(len(all_pixels))
file.close()
base = 0
img_org = np.zeros((1080,1280))
for i in range(len(all_pixels)):
    img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)

img_num = 0
while img_num<13:
    img_num+=1
    while True:
        img = np.zeros((1080,1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255,255,255), -1)

        cv2.imwrite("try1/test_"+str(count)+".png", img)
        count +=1
        cv2.imshow("img", img)
        change = 0
        base+=1
        for i in range(len(all_pixels)):
            if i%base==0 or count>1000100:
                if all_pixels[i][0]!=all_pixels[i][2]:
                    if all_pixels[i][0]<all_pixels[i][2]:
                        all_pixels[i][0]+=1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1]!=all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base==5:
            base = 0

        #print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org-img))==0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k==15:
            break
    img_num+=1

    file = open("edge_BLACK_" + str(2) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080,1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("2",len(lines))
    for line in lines:
        line = line.split()
        if counter<len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.5*64) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.5*64) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.5*64) + 640, int(line[1]) - int(1.5*64) + 540])
        counter+=1

    print(len(all_pixels))
    img_org = np.zeros((1080,1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080,1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255,255,255), -1)

        cv2.imwrite("try1/test_"+str(count)+".png", img)
        count +=1
        cv2.imshow("img", img)
        change = 0
        base+=1
        for i in range(len(all_pixels)):
            if i%base==0 or count>1000200:
                if all_pixels[i][0]!=all_pixels[i][2]:
                    if all_pixels[i][0]<all_pixels[i][2]:
                        all_pixels[i][0]+=1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1]!=all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base==5:
            base = 0

        #print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org-img))==0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k==15:
            break

    img_num+=1


    ###################################################3
    file = open("edge_BLACK_" + str(3) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080,1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("3", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.5*67) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.5*67) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.5*67) + 640, int(line[1]) - int(1.5*67) + 540])
        counter += 1

    print(len(all_pixels))
    img_org = np.zeros((1080,1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080,1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1000350:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1


    ##################################################
    file = open("edge_BLACK_" + str(4) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080,1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("4", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.5*96) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.5*73) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.5*96) + 640, int(line[1]) - int(1.5*73) + 540])
        counter += 1

    print(len(all_pixels))
    img_org = np.zeros((1080,1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080,1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1000500:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1

    ##################################################
    file = open("edge_BLACK_" + str(5) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080,1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("4", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.5 * 108) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.5 * 77) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.5 * 108) + 640, int(line[1]) - int(1.5 * 77) + 540])
        counter += 1

    print(len(all_pixels))
    img_org = np.zeros((1080,1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080,1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1000650:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1

    ##################################################
    file = open("edge_BLACK_" + str(6) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((540, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("6", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.25*164) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.25*95) + 540
        else:
            print("no")
            all_pixels.append([640, 540, int(line[0]) - int(1.25*164) + 640, int(line[1]) - int(1.25*95) + 540])
        counter += 1
    print("AAAAAAAAAAAAAA",counter,len(all_pixels))

    for kk in range(counter,len(all_pixels)):
        all_pixels[kk][2] =  all_pixels[int((counter+1)/2)][2]
        all_pixels[kk][3] =  all_pixels[int((counter+1)/2)][3]
        #print(kk)
        #del all_pixels[counter]

    print(len(all_pixels))

    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1000800:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1

    ##################################################
    file = open("edge_BLACK_" + str(7) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("7", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.25*189) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.25*142) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.25*189) + 640, int(line[1]) - int(1.25*142) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter+1)/2)][2]
        all_pixels[kk][3] = all_pixels[int((counter+1)/2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1000950:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1
    #break
    ##################################################
    file = open("edge_BLACK_" + str(8) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("8", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.25*198) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.25*185) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.25*198) + 640, int(line[1]) - int(1.25*185) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter+1)/2)][2]
        all_pixels[kk][3] = all_pixels[int((counter+1)/2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1001100:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1

    ##################################################
    file = open("edge_BLACK_" + str(9) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("9", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.25*225) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.25*184) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.25*225) + 640, int(line[1]) - int(1.25*184) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter + 1) / 2)][2]
        all_pixels[kk][3] = all_pixels[int((counter + 1) / 2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1001250:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1



    ################################################################
    file = open("edge_BLACK_" + str(10) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("10", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.05 * 355) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.05 * 325) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.05 * 355) + 640, int(line[1]) - int(1.05 * 325) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter + 1) / 2)][2]
        all_pixels[kk][3] = all_pixels[int((counter + 1) / 2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1001400:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1


    ##################################################
    file = open("edge_BLACK_" + str(11) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("11", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(1.05 * 459) + 640
            all_pixels[counter][3] = int(line[1]) - int(1.05 * 335) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(1.05 * 459) + 640, int(line[1]) - int(1.05 * 335) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter + 1) / 2)][2]
        all_pixels[kk][3] = all_pixels[int((counter + 1) / 2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1001550:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1

    ##################################################
    file = open("edge_BLACK_" + str(12) + ".txt", "r")
    for i in range(50):
        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
    img = np.zeros((1080, 1280))

    lines = file.readlines()
    file.close()
    counter = 0
    print("11", len(lines))
    for line in lines:
        line = line.split()
        if counter < len(all_pixels):
            all_pixels[counter][2] = int(line[0]) - int(2 * 296) + 640
            all_pixels[counter][3] = int(line[1]) - int(2 * 242) + 540
        else:
            all_pixels.append([640, 540, int(line[0]) - int(2 * 296) + 640, int(line[1]) - int(2 * 242) + 540])
        counter += 1
    for kk in range(counter, len(all_pixels)):
        all_pixels[kk][2] = all_pixels[int((counter + 1) / 2)][2]
        all_pixels[kk][3] = all_pixels[int((counter + 1) / 2)][3]

    print(len(all_pixels))
    img_org = np.zeros((1080, 1280))
    for i in range(len(all_pixels)):
        img_org = cv2.circle(img_org, (all_pixels[i][2], all_pixels[i][3]), 1, (255, 255, 255), -1)
    while True:
        img = np.zeros((1080, 1280))
        for i in range(len(all_pixels)):
            img = cv2.circle(img, (all_pixels[i][0], all_pixels[i][1]), 1, (255, 255, 255), -1)

        cv2.imwrite("try1/test_" + str(count) + ".png", img)
        count += 1
        cv2.imshow("img", img)
        change = 0
        base += 1
        for i in range(len(all_pixels)):
            if i % base == 0 or count > 1001750:
                if all_pixels[i][0] != all_pixels[i][2]:
                    if all_pixels[i][0] < all_pixels[i][2]:
                        all_pixels[i][0] += 1
                    else:
                        all_pixels[i][0] -= 1
                    change = 1
                if all_pixels[i][1] != all_pixels[i][3]:
                    if all_pixels[i][1] < all_pixels[i][3]:
                        all_pixels[i][1] += 1
                    else:
                        all_pixels[i][1] -= 1
                    change = 1

        if base == 5:
            base = 0

        # print(np.sum(np.sum(cv2.subtract(img_org, img))))
        if np.sum(np.sum(img_org - img)) == 0:
            cv2.imwrite("test.png", img)
            break

        k = cv2.waitKey(2)

        if k == 15:
            break

    img_num += 1