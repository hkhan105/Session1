import cv2

vidCap = cv2.VideoCapture(0)
text = True
while text:
    ret, img = vidCap.read()
    img2 = img[:,::-1,:]
    cv2.imshow("Webcam", img2)
    x= cv2.waitKey(10)
    userChar = chr(x and 0xFF)
    if userChar == 'q':
        text = False
    elif userChar == 'w':
        cv2.imwrite('ss.jpg',img2)


cv2.destroyAllWindows()
vidCap.release()