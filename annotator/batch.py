from Annotator import Annotator
import os
import sys

__author__ = "Jey Kumar"

INPUT_PATH = "input//"

files = os.listdir(INPUT_PATH)
files = sorted(files)

instructions = """
INSTRUCTIONS:
    1. Use your mouse/touchpad to draw rectangles around regions of interest.
    2. Press the matching number on your keyboard as per the instructions on the pop up.
       Press 0 to undo the rectangle.
    3. Repeat steps 1-2 for each remaining region of interest.
    4. Press Space when done. The next image, if any, will now be displayed. See step 1.

NOTES:
    -  If you made a mistake labelling (at step 2), follow these steps:
        (a) Switch to Terminal / Command Prompt and press Ctrl-C to break the loop.
        (b) Go to the "output" folder to see the last file that was successfully annotated.
        (c) Restart the program with the file name from (b) as an additional argument.
            - Example: 'python batch.py frame_100.jpg'
    - If you think something's wrong, call a CV member for help!
"""

print instructions

if len(sys.argv) > 1:
    if sys.argv[1] == "help" or sys.argv[1] == "-help":
        exit()

if len(sys.argv) > 1: # Start at specific image
    start_index = files.index(sys.argv[1])
else: # Start at top
    start_index = 0

for filename in files[start_index:]:
    image = os.path.join(INPUT_PATH, filename)
    annotator = Annotator(image)
    annotator.main()
 
print "ANNOTATION COMPLETED."