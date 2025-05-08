import tkinter as tk

def add():
    result = float(entry1.get()) + float(entry2.get())
    result_label.config(text="Result: " + str(result))

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    result_label.config(text="Result: " + str(result))

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    result_label.config(text="Result: " + str(result))

def divide():
    num2 = float(entry2.get())
    if num2 != 0:
        result = float(entry1.get()) / num2
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Cannot divide by zero")

# GUI window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="+", width=5, command=add).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=subtract).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=multiply).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=divide).grid(row=2, column=1, padx=5, pady=5)

# Result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()
