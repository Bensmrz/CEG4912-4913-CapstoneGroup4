import os, cv2, time
from aiglass_ai_fxns import *
import mediapipe as mp 
import numpy as np

#PARAMETERS
camera = 2
keyword = "NO_HANDS"
no_images = 50
IMG_DIR = "./photos"
NUMPY_PATH = "./numpy"
offset = 0

#VARIABLES


#TEST AND CREATE FOLDER
cap = cv2.VideoCapture(camera)

if not os.path.exists(os.path.join(IMG_DIR, keyword)):
    os.makedirs(os.path.join(IMG_DIR, keyword))


#START CAMERA
counter = 1
while True:
    rect, frame = cap.read()
    cv2.putText(frame, f"Taking pictures of {keyword}: {counter}/{no_images}", (100, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break
    
    #CAPTURE FRAMES ON BUTTON PRESS
    if cv2.waitKey(25) == ord('c'):
        if counter < no_images:
            for i in range(no_images):
                rect, frame = cap.read()
                cv2.putText(frame, f"Taking pictures of {keyword}: {counter}/{no_images}", (100, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
                cv2.imshow('frame', frame)
                cv2.waitKey(500)
                cv2.imwrite(os.path.join(IMG_DIR, keyword, '{}.jpg'.format(counter)), frame)
                counter += 1
        else:
            cv2.putText(frame, f'Already have {counter} captures. Press "q" to quit', (100, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            if cv2.waitKey(25) == ord('q'):
                break


mp_holistic = mp.solutions.holistic # Holistic model
holistic_model = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

#NUMPY GENERATION
for dir_ in os.listdir(IMG_DIR):
    counter = 1
    for img_path in os.listdir(os.path.join(IMG_DIR, dir_)):
        img = cv2.imread(os.path.join(IMG_DIR, dir_, img_path))

        #ret, frame = img.read()
        image, results = mediapipe_detection(img, holistic_model)

        if not os.path.exists(os.path.join(NUMPY_PATH, keyword)):
            os.makedirs(os.path.join(NUMPY_PATH, keyword))

        keypoints = extract_keypoints(results)
        npy_path = os.path.join(NUMPY_PATH, keyword, f"{counter}")
        np.save(npy_path, keypoints)
        counter += 1