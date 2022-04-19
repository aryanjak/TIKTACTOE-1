from cProfile import label
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title(":) KATA (X)  ZERO(O) :)")


def buttonclicked():
    pass


plA = StringVar()
plB = StringVar()
P1 = StringVar()
p2 = StringVar()


p1_name = Entry(tk, textvariable=P1)
p1_name.grid(row=1, column=1, columnspan=8)
p2_name = Entry(tk, textvariable=p2)
p2_name.grid(row=2, column=1, columnspan=8)


label = Label(tk, text="Player 1 : ",
              font="Times 20 bold", bg="white", fg="black")
label.grid(row=1, column=0)
label = Label(tk, text="Player 2 : ",
              font="Times 20 bold", bg="white", fg="black")
label.grid(row=2, column=0)


button1 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button1.grid(row=3,column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button2.grid(row=4,column=0)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button3.grid(row=5,column=0)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button4.grid(row=3,column=1)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button5.grid(row=4,column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button6.grid(row=5,column=1)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button7.grid(row=3,column=2)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button8.grid(row=4,column=2)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="grey", fg="white",
                 height=4, width=8, command=lambda: buttonclicked(button1))
button9.grid(row=5,column=2)




tk.mainloop()
