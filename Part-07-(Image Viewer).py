from tkinter import *
from os import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

def show(pth):
    global img, labelimg, inx
    img = ImageTk.PhotoImage(Image.open(pth))
    labelimg = Label(image=img)
    labelimg.grid(columnspan=2, row=0, column=0)

def locator(carry):
    global piclistaccs
    if carry=='+':
        piclistaccs+=1
    else:
        piclistaccs-=1


slocation = path.dirname(path.abspath(__file__)) # make a list of the other files/folders on the same directory
iteamlist = listdir(slocation)
piclist = []
for i in iteamlist:
    if (str(i)[-3:])=="png":
        piclist.append(i)
print(piclist)

piclistaccs = 0

button_next = Button(root, text="<<", command=lambda: (show(piclistaccs), locator("+")))
button_next.grid(row=1, column=0)                     
button_back = Button(root, text=">>", command=lambda: (show(piclistaccs), locator("-")))
button_back.grid(row=1, column=1)
          
root.mainloop()
