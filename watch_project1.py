from cProfile import label
from cgitb import text
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("HASHMI CLOCK")

def time():
    string=strftime("%H:%M:%S: %p")
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("Algerian", 120), background="blue", foreground="red")

label.pack(anchor="center")
time()
mainloop()
