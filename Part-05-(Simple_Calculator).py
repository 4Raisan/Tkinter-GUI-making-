from tkinter import *
root = Tk()

# root.title(), like the window name in the close button row
root.title('Cal : )')

# input
e = Entry(root, width=20)
e.grid(row=0, column=0, columnspan=4)
#e.pack() use grids to simply design

# process as defs (+,-,/,*)

# buttons with positions, use grid()
# numbers
btnnums = [['1',1,0], ['2',1,1], ['3',1,2], ['4',1,3], ['5',2,0], ['6',2,1], ['7',2,2], ['8',2,3], ['9',3,0], ['0',3,1]]
for (txt, r, c) in btnnums:
  btn = Button(root, text=txt)
  btn.grid(row=r, column=c)
# arithmetic operators and .
btnarm = [['*',4,0], ['/',4,1], ['+',4,2], ['-',4,3], ['.',5,0]]

  
# specials


root.mainloop()
