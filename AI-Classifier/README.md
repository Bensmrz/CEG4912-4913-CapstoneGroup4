# CEG4912-4913-CapstoneGroup4

This project demonstrates object detection using MediaPipe Hands for recognizing hand gestures and mapping them to predefined labels (A, B, C, etc.).

**Project Structure** <br />
The project consists of the following files and directories: <br />

collect_imgs.py: This script is used for collecting and storing training data. <br />
create_dataset.py: This script is used to create a dataset using the collected images. <br />
train_classifier.py: This script is used to train the model on hand gesture data. <br />
inference_classifier.py: This script captures real-time video feed from the webcam and predicts hand gestures using the trained model.

**How to Use**
1. Collect Training Data
To collect training data for each hand gesture, follow these steps:
  - Run the collect_imgs.py script.
  - Press "Q" to start recording data.
  - Capture images of each hand gesture by pressing "Q" again to stop recording for each gesture.
  - Repeat these steps for each gesture class (A, B, C, etc.). The captured images will be saved in the ./data directory under their respective class folders.

2. Create Data Set
To create the data set, follow these steps:
  - Run the create_dataset.py script.
  - A new pickle file will appear in the same directory named data.pickle.

3. Train the Model
After collecting the training data, you can train the model using the train_classifier.py script. Here's how to do it:
  - Run the train_classifier.py script to train the model classifier.
  - The trained model will be saved as model.p.

4. Real-time Prediction
To perform real-time prediction of hand gestures using the trained model, follow these steps:
  - Run the inference_classifier.py script.
  - The webcam feed will start, and the predicted hand gesture will be displayed in real-time.


**Dependencies**<br />
Make sure you have the following dependencies installed before running the code: <br />

Python 3.x <br />
OpenCV <br />
MediaPipe <br />
NumPy <br />
Scikit-Learn <br />

**You can install these dependencies using pip:** <br />
pip install opencv-python mediapipe numpy scikit-learn matplotlib
