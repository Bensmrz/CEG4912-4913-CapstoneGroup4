from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard

from aiglass_ai_fxns import *
import aiglass_ai_vars as vars

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

sequences, labels = [], []
for action in vars.actions:
    for sequence in range(1, vars.no_sequences+1):
        window = []
        for frame_num in range(vars.sequence_length):
            res = np.load(os.path.join(vars.DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(vars.label_map[action])

X = np.array(sequences)
y = to_categorical(labels).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(vars.actions.shape[0], activation='softmax'))

try:
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.fit(X_train, y_train, epochs=2000, callbacks=[tb_callback])
    model.summary()
    model.save('asl_model.keras')
    print('(Full:NoInterrupt) Output saved to asl_model.keras')
    sys.exit()
except KeyboardInterrupt:
    model.summary()
    model.save('asl_model.keras')
    print('(KeyboardInterrupt) Output saved to asl_model.keras')
    


