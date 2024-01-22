from tkinter import *
from tkinter import ttk

def show_message():
    label['text'] = entry.get()
root = Tk()
root.title('Test program')
root.geometry('500x500')


entry = ttk.Entry()
entry.pack(anchor=N, padx=6, pady=6)

btn = ttk.Button(text='Click', command=show_message)
btn.pack(anchor=N, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=N, padx=6, pady=6)

root.mainloop()

