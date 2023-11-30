import os, cv2, time
from aiglass_ai_fxns import *
import aiglass_ai_vars as vars 
import mediapipe as mp 
import numpy as np

#PARAMETERS
camera = vars.camera
keyword = vars.word_being_captured
no_images = vars.num_of_images
IMG_DIR = vars.IMG_PATH
NUMPY_PATH = vars.NUMPY_PATH
offset = vars.capture_offset


#TEST AND CREATE FOLDER
cap = cv2.VideoCapture(camera)

if not os.path.exists(os.path.join(IMG_DIR, keyword)):
    os.makedirs(os.path.join(IMG_DIR, keyword))


#START CAMERA
counter = 1 + offset
while True:
    rect, frame = cap.read()
    if counter < no_images:
        msg = f"Taking pictures for [{keyword}]: {counter}/{no_images}"
    else:
        msg = f"Taking pictures for [{keyword}]: DONE"

    cv2.putText(frame, msg, (100, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (40, 180, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
    
    #CAPTURE FRAMES ON BUTTON PRESS
    if cv2.waitKey(10) == ord('c'):
        if counter <= no_images:
            rect, frame = cap.read()
            cv2.imwrite(os.path.join(IMG_DIR, keyword, '{}.jpg'.format(counter)), frame)
            counter += 1
            
            
        else:
            cv2.putText(frame, f'Already have {no_images} captures. Press "q" to quit', (100, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (40, 180, 0), 3, cv2.LINE_AA)
            if cv2.waitKey(25) == ord('q'):
                break


#DATA AUGMENTATION: