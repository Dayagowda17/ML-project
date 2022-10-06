import numpy as np
import cv2
img=np.zeros([1000,1000,3])
cv2.rectangle(img,(200,200),(700,700),(0,255,0),25)
cv2.imshow('rectangle sqare',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
