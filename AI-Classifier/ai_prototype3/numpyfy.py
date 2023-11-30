import os, cv2, time
from aiglass_ai_fxns import *
import aiglass_ai_vars as vars 
import mediapipe as mp 
import numpy as np

mp_holistic = mp.solutions.holistic # Holistic model
holistic_model = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
IMG_DIR = vars.IMG_PATH
NUMPY_PATH = vars.NUMPY_PATH

#NUMPY GENERATION
for dir_ in os.listdir(IMG_DIR):
    counter = 1
    for img_path in os.listdir(os.path.join(IMG_DIR, dir_)):
        img = cv2.imread(os.path.join(IMG_DIR, dir_, img_path))

        #ret, frame = img.read()
        image, results = mediapipe_detection(img, holistic_model)

        if not os.path.exists(os.path.join(NUMPY_PATH, dir_)):
            os.makedirs(os.path.join(NUMPY_PATH, dir_))

        keypoints = extract_keypoints(results)
        npy_path = os.path.join(NUMPY_PATH, dir_, f"{counter}")
        np.save(npy_path, keypoints)
        counter += 1