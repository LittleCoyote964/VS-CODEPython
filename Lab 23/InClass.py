import tkinter as tk
import tkinter.font as tkFont

w = tk.Tk()
w.geometry("500x100+400+300")#to set up the box for the text
fontStyle = tkFont.Font(family="Times New Roman", size=20)# change the font
fontStyle2 = tkFont.Font(family="Yu Gothic", size=10)
hello = tk.Label(text ="Hello, Nick", font=fontStyle)# text
test = tk.Label(text ="This is a test", font=fontStyle2)#second text
hello.pack()
test.pack()
w.mainloop()