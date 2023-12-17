import sounddevice as sd
import numpy as np
import pygame
import tkinter as tk
from threading import Thread

# Global variables
listening = False
listener_thread = None
counter = 0

# Function to play a sound
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('bruh.mp3')  # Replace with your sound file path
    pygame.mixer.music.play()

# Define a callback function to process the audio stream
def audio_callback(indata, frames, time, status):
    global counter
    volume_norm = np.linalg.norm(indata) * 10  # Calculate the volume level

    threshold = 40 # decibles

    if volume_norm > threshold :  # Check if volume exceeds threshold 
        play_sound()  # Play the sound
        counter += 1  # Increment the counter when noise is detected
        update_counter()
        sd.sleep(750)  # Adjust as needed

# Function to update the counter label in the GUI
def update_counter():
    counter_label.config(text=f"Detected Noises: {counter}")

# Function to start the microphone listener
def start_listener():
    global listening, listener_thread
    if not listening:
        listening = True
        listener_thread = Thread(target=listen_microphone)
        listener_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        print("Listener started. Listening for sound levels above 10 decibels.")

# Function to stop the microphone listener
def stop_listener():
    global listening
    if listening:
        listening = False
        if listener_thread and listener_thread.is_alive():
            listener_thread.join()
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        print("Listener stopped.")

# Function to handle microphone input
def listen_microphone():
    with sd.InputStream(callback=audio_callback):
        while listening:
            sd.sleep(100)  # Adjust as needed

# Create GUI
root = tk.Tk()
root.title("Microphone Listener")
root.geometry("300x200")

start_button = tk.Button(root, text="Start Listener", command=start_listener)
start_button.pack(pady=(50,0), padx=50)

stop_button = tk.Button(root, text="Stop Listener", command=stop_listener, state=tk.DISABLED)
stop_button.pack(pady=10, padx=50)

counter_label = tk.Label(root, text="Detected Noises: 0")
counter_label.pack(pady=10, padx=50)

# Run the GUI
root.mainloop()
