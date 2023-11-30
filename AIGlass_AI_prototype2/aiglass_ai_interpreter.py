import cv2
import numpy as np 
import os, time

from scipy import stats
from matplotlib import pyplot as plt
from tensorflow.keras import models
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
from aiglass_ai_fxns import *
import aiglass_ai_vars as vars


model = models.load_model("asl_model.keras")
model.summary()


colors = [(245,117,16), (117,245,16), (16,117,245)]

def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame


#plt.figure(figsize=(18,18))
#plt.imshow(prob_viz(res, actions, image, colors))


# 1. New detection variables
sequence = []
sentence = []
word = [" "]
predictions = []
threshold = 0.5

cap = cv2.VideoCapture(2)
# Set mediapipe model 
with vars.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        #print(results)
        
        # Draw landmarks
        draw_styled_landmarks(image, results)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]
        
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(vars.actions[np.argmax(res)])
            predictions.append(np.argmax(res))
            
            
        #3. Viz logic
            if np.unique(predictions[-10:])[0]==np.argmax(res): 
                if res[np.argmax(res)] > threshold: 
                    
                    if len(sentence) > 0: 
                        if vars.actions[np.argmax(res)] != sentence[-1]:
                            word[0] = vars.actions[np.argmax(res)]
                            sentence.append(vars.actions[np.argmax(res)])
                    else:
                        word[0] = vars.actions[np.argmax(res)]
                        sentence.append(vars.actions[np.argmax(res)])

            if len(sentence) > 5: 
                sentence = sentence[-5:]

            # Viz probabilities
            #image = prob_viz(res, vars.actions, image, colors)
            
        cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
        #cv2.putText(image, ' '.join(sentence), (3,30),
        cv2.putText(image, ' '.join(word), (3,30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()