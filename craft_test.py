import cv2
import numpy as np
import craft_text_detector
# Create a blank image
img_name="book.png"
img =cv2.VideoCapture(0)
craft = craft_text_detector.Craft(output_folder="final_outputs",crop_type="box", cuda=True)
# Your rectangle coordinates
# Format appears to be [top-left, bottom-right] coordinates
# rectangles = craft_text_detector.predict()
# # Drawing rectangles
# for rect in rectangles:
#     # Extract coordinates
#     x1, y1, x2, y2 = rect
    
#     # Convert to integers as OpenCV requires integer coordinates
#     x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
#     # Draw the rectangle
#     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red color, 2px thickness

# # If you want to handle the nested array format from your example:
nested_rectangles = craft.detect_text(img_name)
# Drawing rectangles from the nested format

