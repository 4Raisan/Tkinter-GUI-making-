from tkinter import *
from os import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

slocation = path.dirname(path.abspath(__file__))
# make a list of the other files/folders on the same directory
iteamlist = listdir(slocation)

img1 = ImageTk.PhotoImage(Image.open("Part-06-(Image).png"))
labelI = Label(image=img1)
labelI.grid(row=0, column=0)

'''button_next = Button(root, text="<<", command=#)
button_next.grid(row=1, column=0)                     
button_back = Button(root, text=">>", command=#)
button_back.grid(row=1, column=1)'''
          
root.mainloop()
