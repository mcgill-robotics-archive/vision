#!/bin/python2.7
import numpy as np
import cv2

import sys,os

def create_kernel(size,in_rad,out_val,in_val,gaussian=False):
        if size%2 == 0:
		raise ValueError('Invalid kernel size')
        if gaussian:
            return get_gaussian(size,size,0.01)

	mid = size/2+1
	ker = np.full((size,size),out_val,dtype=np.float)
	#ker[mid-in_rad-1:mid+in_rad,mid-in_rad-1:mid+in_rad].fill(in_val)
	return ker

def conv(ker,img):
        return cv2.filter2D(img,-1,ker)

def get_gaussian(x,y,std_dev):
    x_orig = x/2.0
    y_orig = y/2.0

    d = np.zeros((x,y))
    for i in xrange(x):
        xcoord = i - x_orig
        for j in xrange(y):
            ycoord = j - y_orig
            

            d[i,j] = 1/(np.pi*2*std_dev**2) * np.exp((xcoord**2+ycoord**2)/(50000*std_dev**2))
            if d[i,j] < 0.005:
                d[i,j] = -d[i,j]
    print d
    return d
def peak_find(image):
        max_pix = 0
        for i in image:
            for b in i:
                if max_pix < b:
                    max_pix = b
        print max_pix
        y = 0
        x = 0
        for i in image:
            y += 1
            for b in i:
                x+=1

                if b == max_pix:
                    break
            else:
                x = 0
                continue
            break
        return (x,y)
        
        
def buoy_filter():
    	img = cv2.imread(sys.argv[1])
    	ker = create_kernel(101,50,6,6)
        print ker
    	img = np.float32(img)/255
    	out_r = conv(ker,img[:,:,2])
    	out_b = conv(ker,img[:,:,0])
    	out_g = conv(ker,img[:,:,1])
    	out = cv2.merge((out_b,out_g,out_r))
    	out_m = np.hstack([img,out])
        cv2.imwrite('features.jpg',np.uint8(out*255)[:,:,2])
        img = np.uint8(img*255)

        loc = peak_find(out[:,:,2])
        print loc
        cv2.circle(img,loc,5,(128,0,255),thickness = -1)
        cv2.imwrite('BuoyLoc.jpg',img)
if __name__ == '__main__':
	buoy_filter()
