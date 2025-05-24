from tkinter import *
from os import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")


def show(pth):
    global img, labelimg
    img = ImageTk.PhotoImage(Image.open(piclist[pth]))
    labelimg = Label(image=img)
    labelimg.grid(columnspan=2, row=0, column=0)

def locator(carry):
    global piclistaccs
    if carry=='+' and piclistaccs<(len(piclist)-1):
        piclistaccs+=1
    elif carry=="-" and piclistaccs>0:
        piclistaccs-=1


slocation = path.dirname(path.abspath(__file__)) # make a list of the other files/folders on the same directory
iteamlist = listdir(slocation)
piclist = []

picformats = ["jpeg","tiff","webp",".jpg",".png",".gif",".bmp",".tif"]
for i in iteamlist:
    for f in picformats:
        if (i[-4:]==f):
            piclist.append(i)
print(piclist)


piclistaccs = 0
show(piclistaccs) # 1st image call
button_next = Button(root, text=">>", command=lambda: (locator("+"), show(piclistaccs)))
button_next.grid(row=1, column=1)                     
button_back = Button(root, text="<<", command=lambda: (locator("-"), show(piclistaccs)))
button_back.grid(row=1, column=0)

root.mainloop()
