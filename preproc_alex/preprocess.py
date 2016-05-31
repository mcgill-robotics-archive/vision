import cv2
import numpy as np
import sys
import cv2.cv as cv

def main(source): 
	src_img = cv2.imread(source)
	out_img, scaleFactor = downsample(src_img,forceDim=True)
	cv2.imshow('input', out_img)
	out_img = contrastStretch(out_img)
	out_img = smoothing(out_img,5)
	#out_img = highPassFilter(out_img)
	cv2.imshow('stretch', out_img)

	outFilePath = 'img/processed/' + sys.argv[1][4:12] + '_out.jpg'

	cv2.waitKey(0)
	cv2.destroyAllWindows

def contrastStretch(src):
	channels = cv2.split(src)
	#channels[0] = cv2.equalizeHist(channels[0])
	channels[1] = cv2.equalizeHist(channels[1])
	channels[2] = cv2.equalizeHist(channels[2])
	merge = cv2.merge(channels)
	return merge

def export(src,out):
	cv2.imwrite(out,src)

def smoothing(source,blurFactor):
	output = cv2.GaussianBlur(source,(blurFactor,blurFactor),0)
	return output

def highPassFilter(src):
	kernel = np.array([[0,1,0],[1,-1,1],[0,1,0]])
	out = cv2.filter2D(src,cv2.CV_8U,kernel)
	return out

def downsample(source,scaleTo=150,forceDim=False):
	#
	# Takes an image source and scales the image to a height
	# of scaleTo (in pixels).
	#
	scale = float(1/float(source.shape[0]))
	if forceDim:
		out_size = (200, 150) #explicit rescale
	else:
		out_size = (int(source.shape[1]*scaleTo*scale),scaleTo) #scale to that varies based on original aspect ratio
	
	output = cv2.resize(source,out_size)
	return output, scale

if __name__ == '__main__':
	main(sys.argv[1])