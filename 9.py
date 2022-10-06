import numpy as np
import cv2
img=cv2.imread('cat.png')
cv2.imshow('RealImage',img)
B,G,R=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('RED',cv2.merge([zeros,zeros,R]))
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.imshow('R&B',cv2.merge([B,R,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()          
