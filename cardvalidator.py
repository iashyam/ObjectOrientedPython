from tkinter import *
from Craditcard import Card

class widget:
    def __init__(self):
        window = Tk()
        window.title("Credit Card validator".title())
        window.geometry('250x150')
        window.minsize(250,150)
        window.maxsize(250,150)
        frame  =LabelFrame(window,padx=20,pady=20)
        frame.pack()
        label = Label(frame,text="Enter Credit Card Number: ",justify=RIGHT)
        label.grid(row=0,column=0,sticky=W, pady=(0,10))
        num = Entry(frame,width=30)
        num.grid(row=1, column=0, pady=(0,10))
        btn = Button(frame, text="Check", command=self.check, cursor='target')
        btn.grid(row=3, column=0)


        window.mainloop()

    def check(self):
        pass


widget()