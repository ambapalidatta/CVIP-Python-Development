import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory

rece = None  # Added variable to store recording data
stop_callback_id = None  # Added variable to store the callback ID


def start_recording():
    global add, rece, stop_callback_id
    add = askdirectory()
    try:
        time = int(sec.get())
        addr = add + "/" + "demo.wav"
        showinfo(title="Start", message="Rec Start")
        rece = sounddevice.rec(time * 44100, samplerate=44100, channels=2, dtype='int16')
        stop_callback_id = win.after(time * 1000, stop_and_save_file)
    except ValueError:
        showwarning(title="Time", message="Wrong Format Time")


def stop_and_save_file():
    global add, rece
    try:
        sounddevice.stop()
        sounddevice.wait()
        write(add + "/" + "demo.wav", 44100, rece)
        showinfo(title="End", message="Rec Stop")
    except AttributeError:
        showwarning(title="Time", message="Recording not started")


def main_window():
    global win, sec
    win = Tk()
    win.geometry("400x250")  # Adjusted window size
    win.resizable(False, False)
    win.title("Voice Recorder")
    win.config(bg="#add8e6")

    sec = Entry(win, font=("Times New Roman", 20))  # Corrected font argument
    sec.place(x=100, y=40, height=50, width=200)  # Adjusted entry position without a gap

    l2 = Label(win, text="Time in Sec.", font=("Times New Roman", 20))  # Corrected font argument
    l2.place(x=100, y=10, height=40, width=200)  # Adjusted label position without a gap

    b = Button(win, text="Record", font=("Times New Roman", 20), command=start_recording)
    b.place(x=150, y=100, height=50, width=100)  # Adjusted button position

    start = Button(win, text="Stop and Save", font=("Times New Roman", 20), command=stop_and_save_file)
    start.place(x=50, y=160, height=50, width=300)  # Adjusted button position to the left for centering

    win.mainloop()


main_window()
