import preprocess as p
import time

def main():
	for r in xrange(1,10):
		hey = time.clock()
		for x in xrange(0,101):
			filePath = 'img/frame' + str(x).zfill(4) + '.jpg'
			p.processWithoutROSConnection(filePath)
		print (time.clock()-hey)/100

if __name__ == '__main__':
	main()