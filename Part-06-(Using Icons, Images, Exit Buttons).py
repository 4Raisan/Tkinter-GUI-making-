from tkinter import *
from PIL import ImageTk,Image   # pip install Pillow - for images

root = Tk()
root.title('Icons & Images & Exit Program')

# add the window icon
root.iconbitmap('Part-06-(iconbitmap).ico')

# add picture
img1 = ImageTk.PhotoImage(Image.open('Part-06-(Image).png'))
