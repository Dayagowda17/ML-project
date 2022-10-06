import cv2
img=cv2.imread('1.jpg',0)
laplacian=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('Laplacian image',laplacian)
canny=cv2.Canny(img,50,200)
cv2.imshow('Canny Image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
