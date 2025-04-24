from pandastable import Table
import tkinter as tk

root = tk.Tk()
root.geometry("650x300")
frame1 = tk.Frame(root, width=400, height=200, bg ="lightblue")
frame1.pack(side=tk.TOP, fill=tk.X)
frame1.pack_propagate(False)
pt = Table(frame1,floatprecision=0)
pt.importCSV('cars.csv')
pt.show()
root.mainloop()