import cv2
import easyocr
import numpy as np

import craft_text_detector

craft = craft_text_detector.Craft(output_dir="cv2_output")


def initialize_ocr():

    return easyocr.Reader(['en'])

def process_frame(frame, reader):
    boxes = craft.detect_text(frame)
    for rect in boxes["boxes"]:
    
        x1, y1 = rect[0]  # Top-left
        x2, y2 = rect[2]  # Bottom-right
        
        # Convert to integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Draw the rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color, 2px thickness
    
    return frame
    # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

    # results = reader.readtext(rgb_frame)
    # for (bbox, text, prob) in results:
    #     if prob > 0.8:  
    #         print(text_list)
    #         print(len(text_list))
    #         (tl, tr, br, bl) = bbox
    #         tl = (int(tl[0]), int(tl[1]))
    #         br = (int(br[0]), int(br[1]))
    #         text_list.append(text)

    #         cv2.rectangle(frame, tl, br, (0, 255, 0), 2)

    #         cv2.putText(frame, text, (tl[0], tl[1] - 10),
    #                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    #         if (len(text_list) > 20):
    #             engine.say(text_list)  
    #             engine.runAndWait()
    #             break
    
    # return frame

def main():
    # Initialize camera and OCR
    cap = cv2.imread('inputs/book.png')

    print("Text detection started. Press 'q' to quit.")
    
    try:
       
            # Capture frame
                        

            processed_frame = process_frame(cap,0 )
            

            cv2.imshow('Text Detection', processed_frame)
            cv2.waitKey(1)
            while True:
                pass
                
    finally:

        
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
