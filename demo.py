import tkinter as t
from time import strftime

root= t.Tk()
root.geometry("500x600")
root.title("Task1: Digital Clock")

def time():
    string =strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)



label = t.Label(root, font=('calibri', 50, 'bold'), background='white', foreground='orange')
label.pack(anchor='center')

time()

root.mainloop()

