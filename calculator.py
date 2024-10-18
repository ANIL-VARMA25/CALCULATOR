import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = option.get()

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

option = tk.StringVar()
option.set("Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.OptionMenu(root, option, *operations).pack()

tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
