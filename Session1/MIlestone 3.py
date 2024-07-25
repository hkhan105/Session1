import cv2
import random
image = cv2.imread('SampleImages/beachBahamas.jpg')

b,g,r = cv2.split(image)
channels = [b,g,r]
random.shuffle(channels)
new_image = cv2.merge(channels)

cv2.imshow('Merged',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()