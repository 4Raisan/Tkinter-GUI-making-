from tkinter import *

root = Tk() # starting

# Just create the Input Box  |  # can't use  hight
e = Entry(root, borderwidth=10, width=50, bg='green', fg='black')

# Add text into input box - Prefilled Input Box
# But u have to clear and give the input, else it's on the output

e.insert(0, 'Enter your name: ')
#e.delete(0, END) # clear the whole input box

e.pack()

root.mainloop() # ending
