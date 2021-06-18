from tkinter import *
from tkinter import messagebox

box = Tk()
box.title("PhoneBook App")

contact_list = {}


def show():
    con = contact_list
    lb = Label(box, text=con)
    lb.grid(row=3, columnspan=2, padx=10, pady=10)


def add():
    nm = e1.get()
    no = e2.get()

    if nm == '' and no == '':
        messagebox.showwarning("Warning", "Please fill the Details")

    if no in contact_list:
        messagebox.showwarning("Warning", "This contact already exists!")
    else:
        contact_list[no] = nm
        e1.delete(0, END)
        e2.delete(0, END)


l1 = Label(box, text='Contact Name : ')
l1.grid(row=0, column=0, padx=5, pady=5)
e1 = Entry(box)
e1.grid(row=0, column=1, padx=5, pady=5)
l2 = Label(box, text='Phone Number : ')
l2.grid(row=1, column=0, padx=5, pady=5)
e2 = Entry(box)
e2.grid(row=1, column=1, padx=5, pady=5)

b = Button(box, text='Show Contact', command=lambda: show())
b.grid(row=2, column=0, padx=10, pady=15, ipadx=5, ipady=5)
b = Button(box, text='Add Contact', command=lambda: add())
b.grid(row=2, column=1, padx=10, pady=15, ipadx=5, ipady=5)

# box.geometry("350x300+0+0")  # 600+200
box.resizable(0, 1)
box.mainloop()
