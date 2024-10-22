import tkinter
from tkinter import *
import math

window = tkinter.Tk()
window.geometry('600x400')
window.title('Pythagorean Theorem Calculator')

entry1 = tkinter.Entry()
entry2 = tkinter.Entry()

def Dawg():
    a = int(entry1.get())
    b = int(entry2.get())
    c = math.sqrt(a**2 + b**2)
    x = math.ceil(c)
    label4.config(text=x)

label1 = tkinter.Label(
    window,
    text="Enter the lengths of the sides of the triangle:",
    font=("Arial Bold", 14)
)

label2 = tkinter.Label(
    window,
    text="Enter the first lenght.",
    font=("Arial Bold", 12)
)

label3 = tkinter.Label(
    window,
    text="Enter the second lenght.",
    font=("Arial Bold", 12)
)

label4 = tkinter.Label(
    window,
    text="Waiting for input",
    font=("Arial Bold", 12)
)

calculatebutton = tkinter.Button(
    window,
    text="Calculate",
    command=Dawg,
)

label1.pack()
label2.pack()
entry1.pack()
label3.pack()
entry2.pack()
calculatebutton.pack(
    padx=20,pady=20
)
label4.pack()
window.mainloop()
