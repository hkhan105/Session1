import cv2
import os

imageNames = os.listdir("SampleImages")
for imageName in imageNames:
    if imageName.endswith(".jpg"):
        cv2.imshow("Image",cv2.imread("SampleImages/"+imageName))
        cv2.waitKey(0)

cv2.destroyAllWindows()