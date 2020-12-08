from tkinter import *
from math import cos, radians
import math

mywindow = Tk()
mywindow.title("Backup Calculator")

mywindow.geometry("390x399")
mywindow.resizable(FALSE,FALSE)

e = Entry(mywindow,width=50,borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_sqrt():
    first_number =e.get()
    global f_num
    global calculate
    calculate = "square root"
    f_num = int(first_number)
    e.delete(0,END)

def button_cos():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "cos operation"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_sin():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "sin operation"
    f_num= int(first_number)
    e.delete(0,END)

def button_log():
    first_number = e.get()
    global f_num
    global calculate
    calculate = "log operation"
    f_num= int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if calculate == "addition":
        e.insert(0,f_num + int(second_number))

    if calculate == "subtraction":
        e.insert(0,f_num - int(second_number))

    if calculate == "multiplication":
        e.insert(0,f_num * int(second_number))

    if calculate == "division":
        e.insert(0,f_num / int(second_number))
    
    if calculate == "square root":
        e.insert(0,f_num ** int(second_number))

    if calculate == "cos operation":
        e.insert(0,math.cos(math.radians(f_num)))

    if calculate == "sin operation":
        e.insert(0, math.sin(math.radians(f_num)))

    if calculate == "log operation":
        e.insert(0, math.log10(f_num))
# Define button

button_1 = Button(mywindow, text="1", padx=40, pady=20, font="Times 12", command=lambda: button_click(1))
button_2 = Button(mywindow, text="2", padx=40, pady=20,font="Times 12", command=lambda: button_click(2))
button_3 = Button(mywindow, text="3", padx=40, pady=20,font="Times 12", command=lambda: button_click(3))
button_4 = Button(mywindow, text="4", padx=40, pady=20,font="Times 12", command=lambda: button_click(4))
button_5 = Button(mywindow, text="5", padx=40, pady=20,font="Times 12", command=lambda: button_click(5))
button_6 = Button(mywindow, text="6", padx=40, pady=20,font="Times 12", command=lambda: button_click(6))
button_7 = Button(mywindow, text="7", padx=40, pady=20,font="Times 12", command=lambda: button_click(7))
button_8 = Button(mywindow, text="8", padx=40, pady=20,font="Times 12", command=lambda: button_click(8))
button_9 = Button(mywindow, text="9", padx=40, pady=20,font="Times 12", command=lambda: button_click(9))
button_0 = Button(mywindow, text="0", padx=40, pady=20,font="Times 12", command=lambda: button_click(0))

button_add = Button(mywindow, text="+", padx=40, pady=20, font="Times 12",bg="#C1CC89",command=button_add)
button_subtract = Button(mywindow, text="-", padx=40, pady=20, font="Times 12",bg="#C1CC89",command=button_subtract)
button_multiply = Button(mywindow, text="*", padx=40, pady=20,font="Times 12",bg="#C1CC89",command=button_multiply)
button_divide = Button(mywindow, text="/", padx=40, pady=20, font="Times 12",bg="#C1CC89",command=button_divide)

button_sqrt = Button(mywindow, text="square root", padx=5, pady=20, font="Times 12",fg="white",bg="#5E7703",command=button_sqrt)
button_cos = Button(mywindow,text="cos", padx=28, pady=20, font="Times 12",fg="white",bg="#5E7703",command=button_cos)
button_sin = Button(mywindow,text="sin", padx=30, pady=20, font="Times 12",fg="white",bg="#5E7703",command=button_sin)
button_log = Button(mywindow, text="log", padx=30,pady=20,font="Times 12",fg="white",bg="#5E7703",command=button_log)

button_equal = Button(mywindow, text="=", padx=39, pady=19,font="Times 12", bg="#6A7D8E", command=button_equal)
button_clear = Button(mywindow, text="CLEAR", padx=22, pady=23, font="Times 10",fg="white",bg="#B06660",command=button_clear)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_sqrt.grid(row=1, column=3)
button_cos.grid(row=2, column=3)
button_sin.grid(row=3, column=3)
button_log.grid(row=4,column=3)

button_equal.grid(row=5, column=0)
button_clear.grid(row=5, column=3)

# Make the program run
mywindow.mainloop()