import tkinter as tk
import tkinter.font as tkFont

w = tk.Tk()
width = w.winfo_screenwidth()
height = w.winfo_screenheight()
w.geometry("600x600")
fontStyle = tkFont.Font(family="Yu Gothic Light", size=20)
hello = tk.Label(text="Nick De Leon",
                 foreground = "Maroon",
                 background = "black",
                 width = 30,
                 height = 10,
                 font=fontStyle)

hello.pack()
w.mainloop()