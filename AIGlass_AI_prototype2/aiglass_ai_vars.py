import numpy as np 
import os, time
import mediapipe as mp

mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

#CONSTANTS AND PATHS:

DATA_PATH = os.path.join('MP_Data')
no_sequences = 30 # Thirty videos worth of data
sequence_length = 30 # Videos are going to be 30 frames in length


#DICTIONARIES
actions = np.array(['A', 'B'])
actions_to_train = np.array(['B'])
label_map = {label:num for num, label in enumerate(actions)}

