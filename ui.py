import os
import tkinter as tk
from tkinter import scrolledtext

from query import getEntry

win = tk.Tk(className='online-dictionary')
win.title("dictionary")

width = 500
height = 300
font = (None, 11)
x = (win.winfo_screenwidth() // 2) - (width // 2)
y = (win.winfo_screenheight() // 2) - (height // 2)
win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#win.resizable(False, False)

def showEntry(event):
    key = word.get()
    with open(os.path.expanduser('~/Documents/vocabulary.txt'),'a') as fo:
        fo.write(key + '\n')
    text = getEntry(key)
    tb.config(state='normal')
    tb.delete(1.0, tk.END)
    tb.insert(tk.INSERT, text)
    tb.config(state='disabled')
win.bind('<Return>', showEntry)

word = tk.StringVar()
ent = tk.Entry(win, text='welcome!', textvariable=word, font=font)
ent.pack(fill='x')

tb = scrolledtext.ScrolledText(win, font=font)
tb.config(state='disabled')
tb.pack(fill='both', expand='yes')

ent.focus()

def run():
    win.mainloop()

if __name__ == '__main__':
    run()
