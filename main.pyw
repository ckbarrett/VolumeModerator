import sounddevice as sd
from playsound import playsound
import numpy as np
from os import system
import tkinter as tk
import _thread as thread

started = False
bruhCount = 0

THRESHOLD = 40

def monitor_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm > THRESHOLD:
        playsound('bruh.mp3')
        global bruhCount 
        bruhCount += 1
        label1 = tk.Label(root, text= 'Bruh Count: ' + str(bruhCount), fg='red', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 250, window=label1)

def startMonitor():
    if started:
        with sd.Stream(callback=monitor_sound):
            sd.sleep(100)
    root.after(1,startMonitor)

def start():  
    label1 = tk.Label(root, text= 'VolumeModerator has Started!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    global started
    started = True

def stop():  
    label1 = tk.Label(root, text= 'VolumeModerator has Stopped!', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    global started
    started = False
   

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

button1 = tk.Button(text='Start',command=start, bg='brown',fg='white')
canvas1.create_window(100, 150, window=button1)

button2 = tk.Button(text='Stop',command=stop, bg='brown',fg='white')
canvas1.create_window(200, 150, window=button2)

# var = tk.IntVar()
# var.set(40)
# scale = tk.Scale( root, variable = var, orient = tk.HORIZONTAL)
# canvas1.create_window(150, 200, window=scale)

root.after(1,startMonitor)

root.mainloop()

