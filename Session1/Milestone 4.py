import cv2
import numpy as np

img = cv2.imread('SampleImages/snowLeo2.jpg')

cv2.putText(img, 'Hello!', (200,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.circle(img,(100,100),100,(0,0,255),-1)
cv2.rectangle(img,(100,100),(200,200),(0,0,255),2)
cv2.ellipse(img,(300,100),(20,40),0,0,320,(0,0,255),-1)

cv2.imshow('Leo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()