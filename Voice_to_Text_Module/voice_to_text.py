#must install speech recog extension in bash with pip install SpeechRecognition

import speech_recognition as sr

name = 'Ben'

def voice_to_text():

    recognizer = sr.Recognizer() #Recognizer instance

    with sr.Microphone() as source: #This is our input driver to capture audio

        print("Hello! My name is " + name + ' and I am ready to help you!')

        try:
            audio_data = recognize.listen(source, timeout=30)
            #print('Debug: Audio Captured Successfully')

            text = recognizer.recognize.google(audio_data) #Google API for Speech recog
            print(f"Text: {text}")
        
        #debugging
        except sr.WaitTimeoutError:
            print('Debug: No audio detected')
        except sr.UnknownValueError:
            print('Debug: Speech recognition could not understand audio')
        except sr.RequestError as e:
            print(f'Debug: Could not collect results from Google API')