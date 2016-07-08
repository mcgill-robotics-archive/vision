import numpy as np
import cv2
import os
import sys

__author__ = "Jey Kumar"

""" Output line format: "(((x1, y1), (x2, y2)), category)",
        where (x1, y1) and (x2, y2) are coordinates of opposing vertices of the region,
        and category is either 1, 2, or 3 (1 = buoy, 2 = bin, 3 = target).
"""

INSTRUCTIONS = "instructions.jpg" # Path to instructions file relative to this script
instructions_file = os.path.relpath(os.path.join(os.path.dirname(__file__), INSTRUCTIONS)) # For cases when script is being imported as module

class Annotator(object):
    """Annotator class"""
    def __init__(self, filename):
        self.filename = filename
        self.img = cv2.imread(filename, -1)
        self.instructions = cv2.imread(instructions_file, -1)
        self.undo = None
        self.pressed = False
        self.need_to_classify = False
        self.clicks = []
        self.regions = []
        self.data = []
        self.key = None

    def display(self):
        # Display output
        cv2.namedWindow("Display")
        cv2.setMouseCallback("Display", self.user_control)
        while True:
            cv2.imshow("Display", self.img)
            key_display = cv2.waitKey(20)
            if key_display & 0xFF == 27: # "Esc" pressed
                break
            elif key_display & 0xFF == 32: # "Space" pressed
                self.dump_data()
                break
            if self.need_to_classify:
                category = None
                cv2.imshow("Display", self.img) # Update window to show drawn rectangle
                cv2.namedWindow("Classify")
                while True:
                    cv2.imshow("Classify", self.instructions)
                    key_classify = cv2.waitKey(20)
                    if key_classify & 0xFF == 49: # "1" pressed
                        category = 1
                        self.classify(category)
                        break
                    elif key_classify & 0xFF == 50: # "2" pressed
                        category = 2
                        self.classify(category)
                        break
                    elif key_classify & 0xFF == 51: # "3" pressed
                        category = 3
                        self.classify(category)
                        break
                    elif key_classify & 0xFF == 48: # "0" pressed
                        self.img = self.undo
                        break
                cv2.destroyWindow("Classify")
                self.need_to_classify = False
                
        cv2.destroyAllWindows()
    
    def user_control(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if not self.need_to_classify:
                del self.clicks[:]
                self.pressed = True
                self.clicks.append((x,y))
        if event == cv2.EVENT_LBUTTONUP:
            if self.pressed and not self.need_to_classify:
                self.clicks.append((x,y))
                pt1 = self.clicks[0]
                pt2 = self.clicks[1]
                self.undo = np.copy(self.img) # backup in case rectangle needs to be redrawn
                cv2.rectangle(self.img, pt1, pt2, (0, 0, 255))
                self.regions.append((pt1, pt2))
                self.need_to_classify = True
                self.pressed = False
    
    def classify(self, category):
        region = self.regions[-1]
        self.data.append((region, category))
        return category
    
    def dump_data(self):
        directory_output = "output\\"
        filename_base = os.path.basename(self.filename).split(".")[0]
        filename_base = os.path.normpath(filename_base + ".txt")
        filename = os.path.join(directory_output, filename_base)
        
        with open(filename, "w") as text_file:
            for region in self.data:
                line = str(region[:]) + "\n"
                text_file.write(line)
        
        msg = "{} annotated.".format(os.path.basename(self.filename))
        print msg

    def main(self):
        self.display()

if __name__ == "__main__":
    """ Instructions:
            1. Click, drag, and release left mouse button to draw a region to annnotate.
            2. Follow on-screen instructions to classify (1 for buoy, 2 for bin, 3 for target, 0 to reset).
            3. When finished, press SPACE to write annotation data to text file (with same file name as input image file).
    """
    filename = sys.argv[1]
    img = Annotator(filename)
    img.main()
    
    
