import time
import tkinter as tk
import speech_recognition as sr

def listen_microphone(label):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Zain")
            label.config(text='Zain')
            label.update()  # Update the label to reflect changes
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            label.config(text=text)
            label.update()  # Update the label to reflect changes

            # Generate timestamp for filename
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{timestamp}.txt"

            # Save text to a file with timestamp as filename
            with open(filename, "a") as file:
                file.write({"content": text, "timestamp": timestamp, "isIncoming": True})

            time.sleep(3)

        except sr.UnknownValueError:
            print("Zain")
            label.config(text="Zain")
            label.update()
        except sr.RequestError as e:
            print("Zain; {0}".format(e))
            label.config(text="Zain")
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
