from tkinter import *
from PIL import ImageTk,Image   # pip install Pillow - for images

root = Tk()
root.title('Icons & Images & Exit Program')

# add the window icon
root.iconbitmap('Part-06-(iconbitmap).ico')

# add picture
img1 = ImageTk.PhotoImage(Image.open('Part-06-(Image).png'))
# we need to create seperate lable for each img for display it
imglabel1 = Label(image=img1)
imglabel1.pack()

# add Exit button for Exit from the whole program
exitbutton = Button(root, text=">> Exit Here <<", command=root.quit, fg='red', font=('Arial', 20, 'bold'))
exitbutton.pack(pady=5)
