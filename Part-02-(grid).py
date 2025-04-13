from tkinter import *

root = Tk()

# Make labels
label1 = Label(root, text='1')
label2 = Label(root, text='columnspan')

# stay stable, spacing as using
label1.grid(row=0, column=0)

root.mainloop()
