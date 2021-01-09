# build simple calculator in tkinter module of python
# Simple operation (+,-,/,*)
# this app is subjects to change in future with more functionality and
# graphics and interactions
#############################################################################
from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define a function for click button
# Set content of entry widget to a var current
# delete entry widget content
# insert current and number in entry widget
def buttonClick(number):
    current = entry.get()
    # delete content in entry widget
    entry.delete(0, END)
    # insert number in entry widget
    entry.insert(0, str(current) + str(number))

# Define a function for clear button to clear all content
def buttonClear():
    entry.delete(0, END)

# Define a function for add button
# set var math as "addition"
# get content of entry widget and store in var fNum
# delete content of entry widget
def buttonAdd():
    firstNumber = entry.get()
    global fNum
    global math
    math = "addition"
    fNum = int(firstNumber)
    entry.delete(0, END)

# Define a function for subtract button
# set var math as "subtraction"
# get content of entry widget and store in var fNum
# delete content of entry widget
def buttonSubtract():
    firstNumber = entry.get()
    global fNum
    global math
    math = "subtraction"
    fNum = int(firstNumber)
    entry.delete(0, END)

# Define a function for Multiply button
# set var math as "multiplication"
# get content of entry widget and store in var fNum
# delete content of entry widget
def buttonMultiply():
    firstNumber = entry.get()
    global fNum
    global math
    math = "multiplication"
    fNum = int(firstNumber)
    entry.delete(0, END)

# Define a function for divide button
# set var math as "division"
# get content of entry widget and store in var fNum
# delete content of entry widget
def buttonDivide():
    firstNumber = entry.get()
    global fNum
    global math
    math = "division"
    fNum = int(firstNumber)
    entry.delete(0, END)

# Define a function for Equal button
# get content of entry widget and store in var secondNumber
# logic to calculate and insert answer in entry widget
#
def buttonEqual():
    secondNumber = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, fNum + int(secondNumber))
    if math == "subtraction":
        entry.insert(0, fNum - int(secondNumber))
    if math == "multiplication":
        entry.insert(0, fNum * int(secondNumber))
    if math == "division":
        entry.insert(0, fNum / int(secondNumber))
# add button widgets for 0-9 and = , +,-,*,/ and clear
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
buttonEqual = Button(root, text="=", padx=91, pady=20, command=buttonEqual)
buttonClear = Button(root, text="Clear", padx=79, pady=20, command=buttonClear)
buttonAdd = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonSubtract= Button(root, text="-", padx=41, pady=20, command=buttonSubtract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
buttonDivide = Button(root, text="/", padx=41, pady=20, command=buttonDivide)
#add buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

root.mainloop()
