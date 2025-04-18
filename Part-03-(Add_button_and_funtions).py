from tkinter import *

root = Tk() # starting

# normal function calling with (), with command no () using
def click():
    labelb = Label(root, text='Clicked..!')
    labelb.pack()
  

# add button
button1 = Button(root, text='Click Here', command=click, padx=5, pady=2, fg='blue', bg='yellow')

# command = function name without ()
button1.pack()

label_or = Label(root, text='OR')
label_or.pack() # just for clearence

def press(i):
    label_2 = Label(root, text=5+i, border=3)
    label_2.pack()

button_2 = Button(root, text="What's 5+7 ?", command=lambda: press(7), border=6, bg='cyan')
button_2.pack()

label_or2 = Label(root, text='OR')
label_or2.pack() # just for clearence

# add Exit button for Exit from the whole program
exitbutton = Button(root, text=">> Exit Here <<", command=root.quit, fg='red', font=('Arial', 20, 'bold'))
exitbutton.pack(pady=5)

root.mainloop() # ending
