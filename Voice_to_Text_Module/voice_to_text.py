import time
import tkinter as tk
import speech_recognition as sr

def listen_microphone(label):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("DEFAULT NAME")
            label.config(text='DEFAULT NAME')
            label.update()  # Update the label to reflect changes
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            label.config(text=text)
            label.update()  # Update the label to reflect changes
            time.sleep(3)
        except sr.UnknownValueError:
            print("DEFAULT NAME")
            label.config(text="DEFAULT NAME")
            label.update()
        except sr.RequestError as e:
            print("DEFAULT NAME; {0}".format(e))
            label.config(text="DEFAULT NAME")
            label.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.geometry('800x600')  # Set window size to 800x600 pixels
    root.configure(bg='black')  # Set window background color to black
    label = tk.Label(root, text="", font=("Helvetica", 48), fg='white', bg='black')
    label.pack(expand=True, fill="both")
    listen_microphone(label)  # Start listening in the window
    root.mainloop()
