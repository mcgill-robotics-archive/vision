import numpy as np
import cv2
import os
import sys

__author__ = "Jey Kumar"


class ImageFeatures(object):
    """ImageFeatures class"""
    def __init__(self, img, hessian=350):
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Load image in B/W
        self.img_colour = img # Load image in colour
        #Added compatibility for opencv 3.X
        if "3." in cv2.__version__:
        	self.surf = cv2.xfeatures2d.SURF_create(hessianThreshold=hessian,upright=True)
        else:
        	self.surf = cv2.SURF(hessian) # Higher threshold returns fewer keypoints (kp)
        	self.surf.getupright = True # 'True' will ignore orientation of kp to increase speed
        self.des = self.get_features(self.img) # Stores feature descriptors
        
    def resize(self, img, x_new, y_new):
	    # Resize image
	    img = cv2.resize(img, (x_new, y_new), interpolation = cv2.INTER_AREA)
	    return img
	    
    def get_features(self, img):
        # Detect keypoints
        kp = self.surf.detect(img)
        # Compute descriptors
        des = self.surf.compute(img, kp)
        return des

    def draw_kp_circles(self, img, des):
        # Draw a small circle at keypoints
        # Radius = 4, red, thickesss = 1
        # Mainly for testing; we can remove this method later
        kp = des[0]
        output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # Convert to colour for circles
        for point in kp:
            (x, y) = point.pt
            cv2.circle(output, (int(x),int(y)), 4, (0, 0, 255), 1)
        return output

    def display(self, img):
        # Display output
        cv2.imshow('Display', img)
        cv2.waitKey(0)
        cv2.destroyWindow('Display')
        
    def save_output(self, img, filename):
        # Save output
        cv2.imwrite(filename, img)
    
    def flatten(self, img):
        # Returns flattened 1-D vector in form of [B1,G1,R1,B2,G2,R2,...]
        return img.flatten()
        
    def filter_kp_in_window(self, x_topleft, y_topleft, x_width, y_width, des):
        # Filter for kp in given region
        x_min, x_max = x_topleft, x_topleft + x_width
        y_min, y_max = y_topleft, y_topleft + y_width
        kp = des[0]
        kp_in_window = []
        for point in kp:
            (x, y) = point.pt
            if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                kp_in_window.append(point)
        return kp_in_window
    
    def compute_avg_des(self, kp_list, des):
        # Compute average descriptor vector for given list of kp
        total_array = np.empty(128) # Assuming extended descriptors, initialize empty array of length 128
        if not kp_list: # If no keypoints are detected
            return total_array # Returns array of zeros
        for point in kp_list:
            index = des[0].index(point)
            total_array += des[1][index]
        average_des = total_array / float(len(kp_list))
        return average_des
        
    def vectorize_window(self, x_topleft, y_topleft, x_width, y_width):
        # Returns flattened image vector concatenated with average descriptor vector for given region
        # Output vector form: [B1,G1,R1,B2,G2,R2,...,Bn,Gn,Rn,D1,D2,...,Dm]]
        crop_img_colour = self.img_colour[y_topleft:y_topleft+y_width, x_topleft:x_topleft+x_width] # Crop given region
        img_vector = crop_img_colour.flatten()
        
        kp_in_window = self.filter_kp_in_window(x_topleft, y_topleft, x_width, y_width, self.des)
        average_des = self.compute_avg_des(kp_in_window, self.des)
        des_vector = average_des.flatten()
        
        window_vector = np.concatenate((img_vector, des_vector))  
        return window_vector
        

class ImageFeaturesLabelled(ImageFeatures):
    def __init__(self, img, annotation, output, hessian=350):
        ImageFeatures.__init__(self, img, hessian)
        self.roi = self.read_annotation(annotation) # regions of interest
        self.filename_annotation = annotation
        self.directory_output = output
        
    def read_annotation(self, annotation):
        with open(annotation, "r") as f:
            data = f.readlines()
            data = [line.strip().replace(" ","") for line in data] # Remove newlines and spaces
            data = [line for line in data if len(line) > 0] # Make sure there are no empty lines
            tuples = [eval(region) for region in data] # Convert string representation of nested tuples to actual nested tuples
            roi = []
            for region in tuples:
                dict = {}
                dict["x_topleft"] = region[0][0][0]
                dict["y_topleft"] = region[0][0][1]
                dict["x_bottomright"] = region[0][1][0]
                dict["y_bottomright"] = region[0][1][1]
                dict["category"] = region[1]
                roi.append(dict)
        return roi
    
    def label_des(self):
        kp = self.des[0]
        buoy_kp = []
        bin_kp = []
        other_kp = []
        
        buoy_des = []
        bin_des = []
        other_des = []
        
        for region in self.roi:
            x_topleft = region["x_topleft"]
            y_topleft = region["y_topleft"]
            x_width = abs(x_topleft - region["x_bottomright"])
            y_width = abs(y_topleft - region["y_bottomright"])
            category = region["category"]
            kp_in_region = self.filter_kp_in_window(x_topleft, y_topleft, x_width, y_width, self.des)
            
            if category == 1: # BUOY
                buoy_kp += kp_in_region
            elif category == 2: # BIN
                bin_kp += kp_in_region
            else:
                print "ERROR: Unrecognized category in annotation data."
                exit()
        other_kp = [point for point in kp if (point not in buoy_kp) and (point not in bin_kp)]

        # Classify keypoints
        for i in range(0, len(kp)):
            if self.des[0][i] in buoy_kp:
                buoy_des.append(self.des[1][i])
            elif self.des[0][i] in bin_kp:
                bin_des.append(self.des[1][i])
            else:
                other_des.append(self.des[1][i])
        
        # Write descriptors to text file
        filename_base = os.path.join(self.directory_output, os.path.basename(self.filename_annotation).split(".")[0])
        filename_base = os.path.normpath(filename_base)
        self.dump_data(filename_base, buoy_des, bin_des, other_des)
        
    def dump_data(self, filename_base, buoy_des, bin_des, other_des):
        filename_buoy = filename_base + "_buoy" + ".txt"
        filename_bin = filename_base + "_bin" + ".txt"
        filename_other = filename_base + "_other" + ".txt"
        
        # Write each set of descriptors to separate text file
        with open(filename_buoy, "w") as text_file:
            for des in buoy_des:
                line = np.array2string(des, precision=20, max_line_width=np.inf, separator=", ", formatter={'float_kind':lambda x: "%.20f" % x}) + "\n"
                text_file.write(line)
        with open(filename_bin, "w") as text_file:
            for des in bin_des:
                line = np.array2string(des, precision=20, max_line_width=np.inf, separator=", ", formatter={'float_kind':lambda x: "%.20f" % x}) + "\n"
                text_file.write(line)
        with open(filename_other, "w") as text_file:
            for des in other_des:
                line = np.array2string(des, precision=20, max_line_width=np.inf, separator=", ", formatter={'float_kind':lambda x: "%.20f" % x}) + "\n"
                text_file.write(line)

if __name__ == "__main__":
    # DEMO
    filename = sys.argv[1]
    img = cv2.imread(filename, -1)
    features = ImageFeatures(img)
    # Display image with circles drawn around keypoints
    output = features.draw_kp_circles(features.img, features.des)
    features.display(output)
    # Print window vector for given region (x_topleft, y_topleft, x_width, y_width)
    window_vector = features.vectorize_window(500, 700, 100, 100) # Left buoy
    print window_vector
