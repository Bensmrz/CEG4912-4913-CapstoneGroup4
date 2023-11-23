import numpy as np 
import os, time

#CONSTANTS AND PATHS:

DATA_PATH = os.path.join('MP_Data')
no_sequences = 30 # Thirty videos worth of data
sequence_length = 30 # Videos are going to be 30 frames in length


#DICTIONARIES
actions = np.array(['hello', 'thanks'])

label_map = {label:num for num, label in enumerate(actions)}

