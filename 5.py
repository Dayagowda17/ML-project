import cv2
img=cv2.imread('1.jpg',0)
cv2.imshow('Grayscale',img)
cv2.waitKey(5000)
man,binary=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow('BINARY IMAGE',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
