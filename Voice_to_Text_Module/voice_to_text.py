import time
import speech_recognition as sr

def listen_microphone():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("DEFAULT NAME")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(text)
            time.sleep(3)
        except sr.UnknownValueError:
            print("DEFAULT NAME")
        except sr.RequestError as e:
            print("Could not complete reques; {0}".format(e))

if __name__ == "__main__":
    listen_microphone()