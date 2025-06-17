import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# 3 Main Messagebox types -------------------------------

# 1. with Info symbole
messagebox.showinfo("Title", "This is an info popup")

# 2. with Warning symbole
messagebox.showwarning("Warning", "This is a warning")

# 3. with Error symbole
messagebox.showerror("Error", "This is an error")

### -----------------------------------------------------

root.mainloop()