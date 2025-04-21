import tkinter as tk
import os
from PIL import Image, ImageTk
top = tk.Tk()
c = tk.Canvas(top, bg='blue', height=872,
width=1329)
print("Current working directory:", os.getcwd()) # had to find where to find in what directory was the code trying to look for the image from. 
load = Image.open("cat.jpg")
img = ImageTk.PhotoImage(load)
c.create_image(1329/2, 872/2, image=img)
c.pack()
top.mainloop()