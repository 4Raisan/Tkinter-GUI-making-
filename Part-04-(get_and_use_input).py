from tkinter import *

root = Tk() # starting

# Just create the Input Box  |  # can't use  hight
e = Entry(root, borderwidth=10, width=50, bg='green', fg='black')

# Add text into input box - Prefilled Input Box
# But u have to clear and give the input, else it's on the output

e.insert(0, 'Enter your name: ')
#e.delete(0, END) # clear the whole input box

e.pack()

e.get() # input for using 

def click():
    label0 = Label(root, text='Hi '+e.get()+'...!') # e.get()
    label0.pack()

    nm = e.get()
    label1 = Label(root, text='Hi'+nm[17:(len(nm))])
    #label1 = Label(root, text='Hi '+e.get()[17:(len(e.get()))]+'...!')
    label1.pack()

    e.delete(0, END) # clear the box forever after the button clicked
    label2 = Label(root, text='Hi '+e.get()+'...!')
    label2.pack()

    # back to normal, above delete deleted forever
    e.insert(0, 'Enter your name: ')

button1 = Button(root, text='Submit', command=click)
button1.pack()

root.mainloop() # ending
