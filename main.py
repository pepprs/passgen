import random as r
import time
from tkinter import *

root = Tk()
root.geometry('800x400')
pw = ""

lbl = Label(root, text="")
lblcopy = Label(root, text="copy")

lowers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
def generate():
    global pw
    pw = ""
    for i in range(16):
        if r.randint(0,4) == 1:
            pw += lowers[r.randint(0,len(lowers) - 1)]
        elif r.randint(0,4) == 2:
            pw += uppers[r.randint(0,len(uppers) - 1)]
        elif r.randint(0,4) == 3:
            pw += nums[r.randint(0,len(nums) - 1)]
        else:
            pw += symbols[r.randint(0,len(symbols) - 1)]
    lbl.config(text=pw)
    lbl.place(x=87,y=50)
def copy():
    root.clipboard_clear()
    root.clipboard_append(pw)
    lblcopy.config(text="Copied!")
    lblcopy.place(x=120,y=130)
    root.after(200,clearlabel)
def clearlabel():
    lblcopy.config(text="")


button = Button(root, text="Generate New", command=generate).place(x=100,y=20)
buttoncopy = Button(root, text="Copy this Password", command=copy).place(x=87,y=100)
buttonexit = Button(root, text="Exit", command=root.quit).place(x=250,y=50)
root.mainloop()

        


