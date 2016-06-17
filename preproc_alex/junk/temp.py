import cv2,sys
import numpy as np

img = cv2.imread(sys.argv[1])
print np.shape(img)
m = np.float32(img)
a,b=cv2.findContours(m[:,:,2],cv2.cv.CV_RETR_EXTERNAL,cv2.cv.CV_CHAIN_APPROX_NONE)
drawn = cv2.drawContours(img,a,-1,(128,128,0))
cv2.imshow(drawn)
cv2.waitKey(0)
cv2.destroyAllWindows()
