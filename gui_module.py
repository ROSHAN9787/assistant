import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3

from intent_model import predict_intent
import api_features as api

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

class AssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Voice Assistant")
        self.root.geometry("520x600")
        self.root.configure(bg="#0f172a")

        title = tk.Label(
            self.root,
            text="AI Voice Assistant",
            font=("Segoe UI", 20, "bold"),
            bg="#0f172a",
            fg="white"
        )
        title.pack(pady=10)

        self.text = scrolledtext.ScrolledText(
            self.root,
            font=("Consolas", 11),
            bg="#020617",
            fg="#38bdf8"
        )
        self.text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.btn = tk.Button(
            self.root,
            text="🎤 Speak",
            font=("Segoe UI", 12, "bold"),
            bg="#22c55e",
            command=self.start_listen
        )
        self.btn.pack(pady=15)

        speak("Hello, I am ready. You can ask me anything.")
        self.root.mainloop()

    def start_listen(self):
        threading.Thread(target=self.listen).start()

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.log("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except:
            speak("Sorry, I did not understand")
            return

    
        self.log("You: " + text)
        text_lower = text.lower()

        # RULE-BASED (STABLE)
        if "time" in text_lower:
            response = api.get_time()

        elif "day" in text_lower or "date" in text_lower:
            response = api.get_day_date()

        elif "open google" in text_lower:
            response = api.open_google()

        else:
            # INTENT + WIKIPEDIA FALLBACK
            response = api.get_wikipedia_info(text)

        self.log("Assistant: " + response)
        speak(response)

    def log(self, msg):
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)

AssistantGUI()
