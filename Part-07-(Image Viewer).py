from tkinter import *
from os import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

def next():
    global img1
    global labelI
    img1 = ImageTk.PhotoImage(Image.open("Part-06-(Image).png"))
    labelI = Label(image=img1)
    labelI.grid(row=0, column=0)

def back():
    global img1
    global labelI
    img1 = ImageTk.PhotoImage(Image.open("Part-06-(Image).png"))
    labelI = Label(image=img1)
    labelI.grid(row=0, column=0)

slocation = path.dirname(path.abspath(__file__))
# make a list of the other files/folders on the same directory
iteamlist = listdir(slocation)
piclist = []
for i in iteamlist:
    if (str(i)[-3:])=="png":
        piclist.append(i)
print(piclist)

img1 = ImageTk.PhotoImage(Image.open("Part-06-(Image).png"))
labelI = Label(image=img1)
labelI.grid(row=0, column=0)

button_next = Button(root, text="<<", command=next)
button_next.grid(row=1, column=0)                     
button_back = Button(root, text=">>", command=back)
button_back.grid(row=1, column=1)
          
root.mainloop()
