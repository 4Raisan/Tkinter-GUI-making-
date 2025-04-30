from tkinter import *
root = Tk()

# root.title(), like the window name in the close button row
root.title('Cal : )')

# input
e = Entry(root, width=20)
e.grid(row=0, column=0, columnspan=4)
#e.pack() use grids to simply design


# process as defs (+,-,/,*)

def allclear():  # all clear the input box
  e.delete(0, END)


# buttons with positions, use grid()
# numbers
btnnums = [['1',1,0], ['2',1,1], ['3',1,2], ['4',1,3], ['5',2,0], ['6',2,1], ['7',2,2], ['8',2,3], ['9',3,0], ['0',3,1]]
for (txt, r, c) in btnnums:
  btn = Button(root, text=txt)
  btn.grid(row=r, column=c)

# arithmetic operators and .
btnarm = [['*',4,0], ['/',4,1], ['+',4,2], ['-',4,3], ['.',5,0]]
for (txt, r, c) in btnarm:
  btn = Button(root, text=txt)
  btn.grid(row=r, column=c)
  
# results and clears
buttonclr = Button(root, text='AC', command=allclear)
buttonclr.grid(row=3, column=2)

buttondel = Button(root, text='⌫')
buttondel.grid(row=3, column=3)

buttoneql = Button(root, text='=')
buttoneql.grid(row=5, column=1, columnspan=3)


root.mainloop()
