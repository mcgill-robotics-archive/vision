import numpy as np
import cv2
import argparse

__author__ = "Jey Kumar"

class ImageFeatures(object):
    """ImageFeatures class"""
    def __init__(self, filename, hessian=350):
        self.img = cv2.imread(filename, 0) # Load image in B/W
        self.img_colour = cv2.imread(filename, -1) # Load image in colour
        self.surf = cv2.SURF(hessian) # Higher threshold returns fewer keypoints (kp)
        self.surf.upright = True # 'True' will ignore orientation of kp to increase speed
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
        output = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) # Convert to colour for circles
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
        
        
if __name__ == "__main__":
    # DEMO
    test = ImageFeatures("test_image.jpg")
    # Display image with circles drawn around keypoints
    output = test.draw_kp_circles(test.img, test.des)
    test.display(output)
    # Print window vector for given region (x_topleft, y_topleft, x_width, y_width)
    window_vector = test.vectorize_window(500, 700, 100, 100) # Left buoy
    print window_vector
