from tkinter import *

def sqnum():
    anum = float(txtEntry.get())
    anum = anum ** 2
    txtDisplay.delete(0,END)
    txtDisplay.insert(0,anum)

mywindow = Tk()
mywindow.title("Windows square demo")
mywindow.geometry("300x200")

txtEntry = Entry(mywindow)
txtEntry.pack()
txtDisplay = Entry(mywindow)
txtDisplay.pack()

btnSqNum = Button(mywindow, text="Square your number", command=sqnum).pack(side=RIGHT)

mywindow.mainloop()




