from tkinter import *

root = Tk()

# TKinter - 1. Define something. 2. Put it on the screen/Root.
myLabel1 = Label(root,text="Hello World")
myLabel2 = Label(root,text="My name is John Doe")
myLabel3 = Label(root,text="              ")
# Declared 2 Labels. Shoving it to the screen in the form of column/row.
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=4)
#  Program ends when loop ends. Program will end when loop ends.
#  The output is relative to each other. For instance if you 
# put label2 on column 5. The output  will appear to be still
# closer to the first column due to the empty columns not 
# being filled any data.
# If a column is left unassigned, it will be ignored. Otherwise, if it is assigned as an empty or blank space, it will be set as that.
# Antidote for this is to add a column with empty details like this:.
myLabel3.grid(row=1,column=1)
root.mainloop()

