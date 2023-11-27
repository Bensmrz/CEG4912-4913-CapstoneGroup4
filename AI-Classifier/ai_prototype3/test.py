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