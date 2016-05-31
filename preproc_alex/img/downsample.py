import cv2

def main():
	for x in xrange(0,120):
		filePath = 'frame' + str(x).zfill(4) + '.jpg'
		src = cv2.imread(filePath)
		out, fes = downsample(src,forceDim=True)
		outFilePath = 'processed/frame' + str(x).zfill(4) + '_downsampled.jpg'
		print outFilePath
		cv2.imwrite(outFilePath, out)

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
	main()