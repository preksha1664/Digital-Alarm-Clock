import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('Digital Clock')

def time():
    string =strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=('Helvetica', 40),foreground='black',background='lightgrey')

label.pack(anchor='center', padx =20, pady =20)


time()
root.mainloop()
