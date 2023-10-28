import random
import string
import tkinter as tk
from tkinter import Label, Entry, Checkbutton, Button

def gen_pass():
    l = int(e.get())
    d = c1.get()
    s = c2.get()

    chars = string.ascii_letters
    if d:
        chars += string.digits
    if s:
        chars += string.punctuation

    p = ''.join(random.choice(chars) for _ in range(l))
    r.config(text="Password: " + p)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")

Label(root, text="Length:").pack()
e = Entry(root)
e.pack()

c1 = tk.IntVar()
Checkbutton(root, text="Digits", variable=c1).pack()

c2 = tk.IntVar()
Checkbutton(root, text="Special Chars", variable=c2).pack()

b = Button(root, text="Generate", command=gen_pass)
b.pack()

r = Label(root, text="")
r.pack()

root.mainloop()