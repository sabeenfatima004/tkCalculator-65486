import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except:
        messagebox.showerror("Error", "Invalid input")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except:
        messagebox.showerror("Error", "Invalid input")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except:
        messagebox.showerror("Error", "Invalid input")

def divide():
    try:
        if float(num2.get()) == 0:
            messagebox.showerror("Error", "Division by zero")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except:
        messagebox.showerror("Error", "Invalid input")

# GUI setup
root = tk.Tk()
root.title("Simple Tkinter Calculator")

tk.Label(root, text="Number 1").grid(row=0, column=0)
tk.Label(root, text="Number 2").grid(row=1, column=0)
tk.Label(root, text="Result").grid(row=2, column=0)

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Entry(root, textvariable=result, state='readonly').grid(row=2, column=1)

tk.Button(root, text="+", command=add).grid(row=3, column=0)
tk.Button(root, text="-", command=subtract).grid(row=3, column=1)
tk.Button(root, text="×", command=multiply).grid(row=4, column=0)
tk.Button(root, text="÷", command=divide).grid(row=4, column=1)

root.mainloop()
