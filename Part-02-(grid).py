from tkinter import *

root = Tk()

# Make labels
label1 = Label(root, text='1')
label2 = Label(root, text='columnspan')
label3 = Label(root, text='2')
label4 = Label(root, text='2i')
label5 = Label(root, text='rowspan')
label6 = Label(root, text='I am here')

# stay stable, spacing as using
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, columnspan=2)

root.mainloop()
