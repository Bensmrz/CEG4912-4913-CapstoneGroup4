import numpy as np 
import os, time
import mediapipe as mp

#IMAGE CAPTURE PARAMETERS
camera = 0
word_being_captured = "C"
num_of_images = 50

IMG_PATH = "./photos"
NUMPY_PATH = "./numpy"
capture_offset = 0




#HOLISTIC MODEL:
mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

#CONSTANTS AND PATHS:

no_sequences = 30 # Thirty videos worth of data
sequence_length = 30 # Videos are going to be 30 frames in length


#DICTIONARIES
actions = np.array(['A', 'B', 'C', 'NO_SIGN'])
actions_to_train = np.array(['B'])
label_map = {label:num for num, label in enumerate(actions)}
