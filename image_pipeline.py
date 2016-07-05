from annotator import Annotator
from features import ImageFeatures
from preproc_alex import preprocess_noROS as preprocess

import cv2
import sys

__author__ = "Jey Kumar"

# Load image
filename_img = sys.argv[1]
img = cv2.imread(filename_img)

# Preprocess image
img_preproc = preprocess.process(img)
img_preproc = cv2.convertScaleAbs(img_preproc) # Convert image to CV_8U to avoid bugs with imshow

# Write feature descriptors to text files (given annotation data)
filename_annotation = sys.argv[2]
directory_output = sys.argv[3]
features = ImageFeatures.ImageFeaturesLabelled(img, filename_annotation, directory_output)
features.label_des()

# Vectorize window?

# Pass data to learner
# Code here