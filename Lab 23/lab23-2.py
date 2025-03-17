import tkinter as tk
import tkinter.font as tkFont

def handle_click():
    Kilo = float(entry1.get())
    Mile = Kilo * 0.621371
    Rlabel.configure(text=f"{Kilo} km = {Mile:.2f} miles")



w = tk.Tk()
w.title("Kilo to Mile")
w.configure(bg="maroon")
w.geometry("600x600")
fontStyle = tkFont.Font(family="Times New Roman", size=20)
label1 = tk.Label(text="Please input a value in Kilometer.", font=fontStyle)
label1.place(x=100, y=100)
entry1 = tk.Entry(fg="maroon", width=10, font=("Times New Roman", 20))
entry1.place(x=240, y=200)
button1 = tk.Button(text="Convert!", width=25, height=5, bg="white", fg="Black", command=handle_click)
button1.place(x=215, y=300)
button1.bind("<Button-1>", handle_click)

Rlabel = tk.Label(text="", font=fontStyle, bg="maroon", fg="white")
Rlabel.place(x=150, y=400)

w.mainloop()