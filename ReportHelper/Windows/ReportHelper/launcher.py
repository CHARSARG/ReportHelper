import os
import tkinter as tk
import tkinter.ttk as ttk
#import main
root = tk.Tk()
root.title("Launcher")
root.geometry("400x400")
canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()
def run():
    root.destroy()
    import main
 
 
start = tk.Button(text='Launch', command=run)
canvas1.create_window(200,200, window=start)

root.mainloop()
