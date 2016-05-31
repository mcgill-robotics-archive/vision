#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import cv2
import sys
import math
import profile
#takes filename to process
#multiplies the intensity of all the pixels by a factor of 1/2
#runs the grayworld algorithm on the image to create input 1
#runs a bilatereal filter then equalizes the histogram to create input 2
#WIP#
#caluclate weightmdaps
#fuse
#output
#WIP#
class image_listener:
    def __init__(self):
        self.image_pub = rospy.Publisher("processed_image",Image,queue_size=10)
        self.image_sub = rospy.Subscriber("/camera_front_left/image_rect_color",Image,self.callback)
        self.bridge = CvBridge()
    def callback(self,data):
        try:
             img = self.bridge.imgmsg_to_cv2(data,'bgr8')
        except CvBridgeError as e:
            print e
        proc_img = process(img)
        try:
            pub_img = self.bridge.cv2_to_imgmsg(proc_img)
        except CvBridgeError as e:
            print e
        self.image_pub.publish(pub_img)


def main():
    #Comment out the top three lines to return this back to normal.
    src_img = cv2.imread(sys.argv[1])
    processed = process(src_img)

    #il = image_listener()
    #rospy.init_node("processer",anonymous = True)
    #rospy.spin()

def processFromFilePath(filePath):
    src_img = cv2.imread(filePath)
    processed = process(src_img)
    return processed

def process(img):
    image = img
    image,_ = downsample(image,150,forceDim=False)
    image = np.float32(image)
    equi_img = image*(2.0/4.0)#halves the intensities
    size_w = np.shape(equi_img)[0]#width
    size_l = np.shape(equi_img)[1]#length
    i1 = grayworld(equi_img)#creates the first input
    equi_img = np.float32(equi_img)#convert the image back into float32
    
    ##### TESTING FILTERS (Currently Gaussian is fastest and removes noise the best - Alex: 1 May 16)
    #i2 = cv2.bilateralFilter(equi_img,11,size_w,size_l)#input 2 created by bilateral filter
    #i2 = cv2.bilateralFilter(equi_img,5,size_w,size_l)
    i2 = cv2.GaussianBlur(equi_img,(5,5),3.0)
    ##### TESTING FILTERS

    i2 = equalhist(i2)#equalize histogram
    #w1 = saliency_weight_map(cv2.GaussianBlur(i2,(11,11),0.3),i2)
    #w2 = saliency_weight_map(cv2.GaussianBlur(i1,(11,11),0.3),i1)
    #p = cv2.addWddeighted(i2,w1,i1,w2)
    fused = fusion(i1,i2)
    compare = np.hstack([image,fused])
    cv2.imwrite("compare.jpg",compare)
    cv2.imwrite("final.jpg",fused)
    cv2.imwrite("i1.jpg",i1)
    cv2.imwrite("i2.jpg",i2)
    return compare
    print "Done!"

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

#grayworld
#take image and split into 3 channels
#sum up the intensities in the image, and put them in a 3-tuple where first
#element is the sum of the intensities of the red channel etc.
#create illumination factor for each channel by taking the earlier sum and
#using sum/(area of the image)
# use the illumination factor and create a scaling factor which is  the mean of
# all the illuminaton factors
# calculate new pixel values according to new = old*scale/illum for each channel
# return new image
def grayworld(image):
    b,g,r = cv2.split(image)
    imsum = cv2.sumElems(image)
    illum = [i/(np.shape(image)[0]*np.shape(image)[1]) for i in imsum]
    scale = (illum[0]+illum[1]+illum[2])/3
    r = (r*scale)*(1/illum[2])
    g = (g*scale)*(1/illum[1])
    b = (b*scale)*(1/illum[0])
    gryw = cv2.merge((b,g,r))
    return gryw
#histogram equalization
#perform contrast adaptive histogram equalization by using similar pixels and 
#creating an averaged picture
#see opencv docs on Contrast Adaptive Histogram Equalization(clahe) for more info
def equalhist(image):
    b,g,r = cv2.split(image)
    b,g,r = np.uint8(b),np.uint8(g),np.uint8(r)
    clahe= cv2.createCLAHE(clipLimit = 8,tileGridSize = (3,3))
    eb,eg,er = clahe.apply(b),clahe.apply(g),clahe.apply(r)
    req = cv2.merge((eb,eg,er))
    return req 
#WIP
#calculatiion of the weight maps for the fusion process

#Laplacian weight
#find the luminance channel of each image
#create a laplacian of the channel
#take the absoulute value of the two laplacians to create the fusion weights
def laplacian_weight(img):
    img = np.float32(img)
    lap_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    vlp = cv2.Laplacian(lap_img[:,:,2],cv2.CV_32F)
    return vlp
def wlc(img):
    img = np.float32(img)
    lim2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    gauss_lim2 = cv2.GaussianBlur(lim2[:,:,2],(5,5),1)
    return lim2[:,:,2]-gauss_lim2
def wexposed(img):
    img = np.float32(img)
    limg = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    img = limg[:,:,2]
    #default sigma
    sigma = 0.25
    ref = np.zeros(np.shape(img))
    ref.fill(0.5)
    diff = img-ref
    scaled = diff*(1/(-2*(sigma*sigma)))
    weight = np.exp(scaled)
    return weight
def saliency_weight_map(blur_img,img):
    weight_map = np.zeros(np.shape(blur_img))
    for x in xrange(np.shape(weight_map)[2]):
        weight_map[x] = a[x]
    return weight_map
#TODO
#Fusion step
# takes two images returns one
# performs weighted addition
def fusion(im1,im2):
    lcm = wlc(im1)
    exw = wexposed(im1)
    lw = laplacian_weight(im1)
    norm_weight = (exw+lw)/2
    
    lcm2 = wlc(im2)
    exw2 = wexposed(im2)
    lw2 = laplacian_weight(im2)
    
    norm_weight2 = (exw2+lw2)/2
    im1_split = []
    im2_split = []
    f1 = []
    
    for a,b in zip(np.transpose(im1),np.transpose(im2)):
        im1_split.append(a)
        im2_split.append(b)
    for x,y in zip(im1_split,im2_split): 
        x = np.transpose(x)
        y = np.transpose(y)
        #fused = np.multiply(x,norm_weight)+np.multiply(y,norm_weight2)
        fused = x+y
        f1.append(fused)
    fused = cv2.merge((f1[0],f1[1],f1[2]))
    return fused
if __name__ == "__main__":
    profile.run('main()')
    
