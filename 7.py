import numpy as np
import cv2
img=np.zeros((500,500,3))
#img[:]=0,1,1
img[:]=255,255,0
cv2.imshow('RGB',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
           
