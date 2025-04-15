from tkinter import *

root = Tk() # starting

# normal function calling with (), with command no () using
def click():
    labelb = Label(root, text='Clicked..!')
    labelb.pack()
  

# add button
button1 = Button(root, text='Click Here', command=click, padx=5, pady=2, fg='blue', bg='yellow')

root.mainloop() # ending
