import tkinter as tk
from PIL import Image, ImageTk
top = tk.Tk()
c = tk.Canvas(top, bg='blue', height=872,
width=1329)
load = Image.open('cat2.jpg')
img = ImageTk.PhotoImage(load)
c.create_image(1329/2, 872/2, image=img)
c.pack()
top.mainloop()