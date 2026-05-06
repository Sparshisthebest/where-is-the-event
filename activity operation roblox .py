from tkinter import *
from tkinter import messagebox
# Setup Tkinter Window
root = Tk()
root.geometry("200x200")
# Function for Displaying Warning Message
# This will be called once the button is clicked
# message.showwarning("warning Name")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")
button = Button(root, text="scan for Virus", command=msg)
button.place(x=40, y=80)
# Entering main event lopp
root.mainloop()