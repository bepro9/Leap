from tkinter import *

box = Tk()
box.title('Calculator')
f1 = Frame(box).pack()


# Action
def solve():
    q = area.get()
    area.delete(0, END)
    ins = eval(q)
    area.insert(0, ins)


def insert_num(x):
    area.insert(END, x)


# field
area = Entry(f1, bd=3, width=29, justify=RIGHT, fg='orange')
area.pack(padx=10, pady=40)

# numbers 
nine = Button(f1, text='9', width=3, height=2, command=lambda: insert_num(9)).place(x=23, y=100)
eight = Button(f1, text='8', width=3, height=2, command=lambda: insert_num(8)).place(x=93, y=100)
seven = Button(f1, text='7', width=3, height=2, command=lambda: insert_num(7)).place(x=163, y=100)
mul = Button(f1, text='*', width=3, height=2, command=lambda: insert_num('*')).place(x=233, y=100)

six = Button(f1, text='6', width=3, height=2, command=lambda: insert_num(6)).place(x=23, y=150)
five = Button(f1, text='5', width=3, height=2, command=lambda: insert_num(5)).place(x=93, y=150)
four = Button(f1, text='4', width=3, height=2, command=lambda: insert_num(4)).place(x=163, y=150)
div = Button(f1, text='/', width=3, height=2, command=lambda: insert_num('/')).place(x=233, y=150)

three = Button(f1, text='3', width=3, height=2, command=lambda: insert_num(3)).place(x=23, y=200)
two = Button(f1, text='2', width=3, height=2, command=lambda: insert_num(2)).place(x=93, y=200)
one = Button(f1, text='1', width=3, height=2, command=lambda: insert_num(1)).place(x=163, y=200)
plus = Button(f1, text='+', width=3, height=2, command=lambda: insert_num('-')).place(x=233, y=200)

zero = Button(f1, text='0', width=3, height=2, command=lambda: insert_num(0)).place(x=23, y=250)
dot = Button(f1, text='.', width=3, height=2, command=lambda: insert_num('.')).place(x=93, y=250)
ans = Button(f1, text='=', width=3, height=2, fg='yellow', command=solve).place(x=163, y=250)
minus = Button(f1, text='-', width=3, height=2, command=lambda: insert_num('-')).place(x=233, y=250)

box.geometry('320x320')
box.resizable(0, 0)
box = mainloop()
