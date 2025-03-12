import tkinter as tk
from tkinter import font
root = tk.Tk()
f = list(font.families())
f.sort()
for i in f:
    print(i)