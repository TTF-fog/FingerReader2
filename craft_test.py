import cv2
import numpy as np
import craft_text_detector
# Create a blank image
img_name="book.png"
img =cv2.VideoCapture(0)
craft = craft_text_detector.Craft(crop_type="box", cuda=True)
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
for rect in nested_rectangles["boxes"]:
    # For this format, we need to extract the corners
    # The format appears to be [top-left, top-right, bottom-right, bottom-left]
    x1, y1 = rect[0]  # Top-left
    x2, y2 = rect[2]  # Bottom-right
    
    # Convert to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    # Draw the rectangle
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color, 2px thickness

# Display the image
cv2.imshow('Rectangles', img)
while True:
    k = cv2.waitKey(0) 
