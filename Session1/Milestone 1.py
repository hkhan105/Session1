import cv2


imageNames = [
    'SampleImages/antiqueTractors.jpg',
    'SampleImages/beachBahamas.jpg',
    'SampleImages/chicago.jpg',
    'SampleImages/Coins/coins2.jpg',
    'SampleImages/Coins/d011arCoin.jpg']
for imageName in imageNames:
    image = cv2.imread(imageName)
    if image is not None:
        cv2.imshow("Images", image)
        cv2.waitKey(0)
    else:
        print("Image not found")

# Close the window
cv2.destroyAllWindows()