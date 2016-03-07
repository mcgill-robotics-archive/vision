#!/bin/python2.7
import numpy as np
import cv2

import sys,os

def create_kernel(size,in_rad,out_val,in_val,gaussian=False):
        if size%2 == 0:
		raise ValueError('Invalid kernel size')
	mid = size/2+1
	ker = np.full((size,size),out_val,dtype=np.float)
	ker[mid-in_rad-1:mid+in_rad,mid-in_rad-1:mid+in_rad].fill(in_val)
	return ker*(1.0/(size*size))
def conv(ker,img):
	out = cv2.filter2D(img,-1,ker)
	return out
def buoy_filter():
	img = cv2.imread(sys.argv[1])
	ker = create_kernel(113,30,-2,6)
	img = np.float32(img)/255
	out_r = conv(ker,img[:,:,2])
	out_b = conv(ker,img[:,:,0])
	out_g = conv(ker,img[:,:,1])
	out = cv2.merge((out_b,out_g,out_r))
	out_m = np.hstack([img,out])

	e2,boring = cv2.findContours(np.uint8(255*out_r),cv2.cv.CV_RETR_EXTERNAL,cv2.cv.CV_CHAIN_APPROX_NONE)
	
	cv2.drawContours(out,e2,-1,(128,128,0),3)
        img = np.uint8(img*255)
        out_e = np.hstack((img,out))
        cv2.imwrite("BuoyLoc.jpg",out_e)
	cv2.imshow('Output Image',out_m)
        cv2.imshow('Edge2',out)
	cv2.waitKey(0)
	cv2.destroyAllWindows
if __name__ == '__main__':
	buoy_filter()
