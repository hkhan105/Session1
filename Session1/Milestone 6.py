# This script shows how to crop a part of an image
import cv2
import numpy as np
# Crop first 100 rows and first 200 columns
image = cv2.imread("SampleImages/canyonlands.jpg")
subImg = image[0:100, 0:200]
cv2.imshow("Subimage", subImg)
# Crop two pictures to just the pixel locs they share
im1 = cv2.imread("SampleImages/grandTetons.jpg")
im2 = cv2.imread("SampleImages/mightyMidway.jpg")
(hgt1, wid1, dep1) = im1.shape
(hgt2, wid2, dep2) = im2.shape
newWid = min(wid1, wid2)
newHgt = min(hgt1, hgt2)
im1Crop = im1[0:newHgt, 0:newWid]
im2Crop = im2[0:newHgt, 0:newWid]
cv2.imshow("Im1 Cropped", im1Crop)
cv2.imshow("Im2 Cropped", im2Crop)
blended = cv2.addWeighted(im1Crop, 0.5, im2Crop, 0.5, 0)
cv2.imshow("Blended", blended)
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
prevPics = [frame]*5
while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    blended = cv2.addWeighted(frame, 0.5, prevPics[1], 0.5, 0)
    cv2.imshow("Blended", blended)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    prevPics.append(frame)
    prevPics.pop(0)

capture.release()
cv2.destroyAllWindows()