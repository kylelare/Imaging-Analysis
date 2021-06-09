import cv2 as cv

#Simple image type conversion using opencv

#Load original image
image = cv.imread('image.png')

#Save converted image
cv.imwrite('image.jpg', image)
