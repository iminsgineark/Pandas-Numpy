from tkinter import *

# import tkinter as Tk

root = Tk()

root.geometry("555x555")
root.minsize(333, 333)
root.maxsize(999, 999)
root.title("UA")
root = Label(text="Hi I'm Utkrist Ark",bg="lightblue",fg="red",padx=3,pady=2)
root.pack()

# image Display
# photo = PhotoImage(file="iker.png")
#
# image_label = Label(image=photo)
# image_label.pack()

root.mainloop()
