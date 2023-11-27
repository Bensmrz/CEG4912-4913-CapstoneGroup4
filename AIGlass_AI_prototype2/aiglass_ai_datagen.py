import cv2
import numpy as np 
import os, time
import mediapipe as mp 
from matplotlib import pyplot as plt

from aiglass_ai_fxns import *
import aiglass_ai_vars as vars


# Folder start
start_folder = 30

for action in vars.actions_to_train: 
    for sequence in range(1, vars.no_sequences+1):
        #dirmax = np.max(np.array(os.listdir(os.path.join(vars.DATA_PATH, action))).astype(int))
        try: 
            #os.makedirs(os.path.join(vars.DATA_PATH, action, str(dirmax+sequence)))
            os.makedirs(os.path.join(vars.DATA_PATH, action, str(sequence)))
        except:
            pass


cap = cv2.VideoCapture(2)
# Set mediapipe model 
with vars.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    # NEW LOOP
    # Loop through actions
    for action in vars.actions_to_train:
        # Loop through sequences aka videos
        for sequence in range(1, vars.no_sequences+1):
            # Loop through video length aka sequence length
            for frame_num in range(vars.sequence_length):

                # Read feed
                ret, frame = cap.read()

                # Make detections
                image, results = mediapipe_detection(frame, holistic)
                #print(results)

                # Draw landmarks
                draw_styled_landmarks(image, results)
                
                # NEW Apply wait logic
                if frame_num == 0: 
                    cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(2000)
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                
                # NEW Export keypoints
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(vars.DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                # Break gracefully
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                    
    cap.release()
    cv2.destroyAllWindows()




